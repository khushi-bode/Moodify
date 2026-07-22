from fastapi import APIRouter, HTTPException, status, Request
from pydantic import BaseModel
from typing import Optional, List, Dict
from app.services.vision import analyze_image, VisionError
from app.services.ai import generate_insight, generate_suggestions
from app.db.supabase_client import get_supabase_client
import random
import time
import concurrent.futures

router = APIRouter()

# Simple in-memory rate limiter
RATE_LIMIT_MAP = {}
MAX_REQUESTS_PER_MINUTE = 10

class ScanRequest(BaseModel):
    image: str
    time_of_day: Optional[str] = "day"

class SuggestionItem(BaseModel):
    id: str
    text: str

class ScanResponse(BaseModel):
    success: bool
    emotion: str
    confidence: int
    summary: str
    insight: str
    suggestions: List[SuggestionItem] = []
    wellness_score: int
    emotion_probabilities: Dict[str, float] = {}

@router.post("/scan", response_model=ScanResponse)
def process_scan(request: Request, scan_request: ScanRequest):
    # Rate Limiting
    client_ip = request.client.host if request.client else "unknown"
    current_time = time.time()
    
    user_rate = RATE_LIMIT_MAP.get(client_ip, {"count": 0, "reset_time": current_time + 60})
    if current_time > user_rate["reset_time"]:
        user_rate = {"count": 1, "reset_time": current_time + 60}
    else:
        user_rate["count"] += 1
        if user_rate["count"] > MAX_REQUESTS_PER_MINUTE:
            raise HTTPException(status_code=429, detail="Too many requests. Please try again later.")
    
    RATE_LIMIT_MAP[client_ip] = user_rate

    try:
        # 1. Run deterministic vision pipeline
        vision_result = analyze_image(scan_request.image)
    except VisionError as e:
        # Return 422 Unprocessable Entity with custom error format
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"error": e.code, "message": e.message}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "INTERNAL_ERROR", "message": "An unexpected error occurred processing your image."}
        )
        
    emotion = vision_result["emotion"]
    
    def get_insight():
        return generate_insight(
            emotion=emotion,
            confidence=vision_result["confidence"],
            time_of_day=scan_request.time_of_day
        )
    
    def get_suggestions():
        base_suggestions = []
        try:
            supabase = get_supabase_client()
            # Query for matching emotion and time_of_day, OR time_of_day = 'any'
            # We'll just fetch all for the emotion and filter in python to be safe with OR logic in postgrest
            response = supabase.table('suggestions').select('*').eq('emotion', emotion).execute()
            
            all_for_emotion = response.data
            if all_for_emotion:
                # Filter by time of day or 'any'
                valid_time = [s for s in all_for_emotion if s.get('time_of_day') == scan_request.time_of_day or s.get('time_of_day') == 'any']
                
                # If none match time exactly, just use any available for that emotion
                if not valid_time:
                    valid_time = all_for_emotion
                    
                # Pick 2 to 4 randomly
                num_to_pick = min(len(valid_time), random.randint(2, 4))
                base_suggestions = random.sample(valid_time, num_to_pick)
                
        except Exception as e:
            print(f"Failed to fetch suggestions from DB: {e}")

        personalized = []
        if base_suggestions:
            personalized = generate_suggestions(
                emotion=emotion,
                mood_score=vision_result["moodScore"],
                time_of_day=scan_request.time_of_day or "day",
                base_suggestions=base_suggestions
            )
        return personalized

    # Run AI insight generation and suggestion personalization concurrently to halve latency
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_insight = executor.submit(get_insight)
        future_suggestions = executor.submit(get_suggestions)
        
        insight_data = future_insight.result()
        personalized = future_suggestions.result()
    
    return ScanResponse(
        success=True,
        emotion=emotion,
        confidence=vision_result["confidence"],
        summary=insight_data["summary"],
        insight=insight_data["insight"],
        suggestions=personalized,
        wellness_score=vision_result["moodScore"],
        emotion_probabilities=vision_result.get("emotion_probabilities", {})
    )
