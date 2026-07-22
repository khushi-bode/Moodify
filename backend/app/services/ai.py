import os
import json
from google import genai
from google.genai import types
from pydantic import BaseModel

def get_ai_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

SYSTEM_PREAMBLE = (
    "You are Moodify's wellness assistant. You are not a medical professional and "
    "never provide diagnosis or medical advice. Keep responses concise, warm, and "
    "non-judgmental. Always be compatible with a visible non-diagnostic disclaimer "
    "shown alongside your output."
)

class EmotionDetectionResult(BaseModel):
    emotion: str
    confidence: int

def detect_emotion_vision(base64_image: str, mime_type: str = "image/jpeg") -> EmotionDetectionResult | None:
    """
    Sends a cropped face image to Gemini Vision to accurately detect the dominant emotion.
    Returns structured data containing emotion and confidence.
    """
    client = get_ai_client()
    if not client:
        return None

    # Supported emotions: Happy, Sad, Angry, Calm, Relaxed, Neutral, Fear, Surprise, Disgust, Anxious
    prompt = (
        "Analyze this closely cropped face image and determine the person's current emotion. "
        "Focus ONLY on their facial expression, completely ignoring lighting, clothing, and background. "
        "Select EXACTLY one of the following emotions: Happy, Sad, Angry, Calm, Relaxed, Neutral, Fear, Surprise, Disgust, Anxious. "
        "If you are highly uncertain, choose Neutral. "
        "Also provide a confidence score from 0 to 100 based on how clear the expression is."
    )
    
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash-lite',
            contents=[
                types.Part.from_bytes(
                    data=base64_image,
                    mime_type=mime_type,
                ),
                prompt
            ],
            config=types.GenerateContentConfig(
                temperature=0.2, # Low temperature for more deterministic classification
                response_mime_type="application/json",
                response_schema=EmotionDetectionResult,
            ),
        )
        
        if response.text:
            data = json.loads(response.text)
            # Ensure the emotion is one of the supported ones and capitalized correctly
            emotion = str(data.get("emotion", "Neutral")).capitalize()
            confidence = int(data.get("confidence", 50))
            
            valid_emotions = ["Happy", "Sad", "Angry", "Calm", "Relaxed", "Neutral", "Fear", "Surprise", "Disgust", "Anxious"]
            if emotion not in valid_emotions:
                emotion = "Neutral"
                
            return EmotionDetectionResult(emotion=emotion, confidence=confidence)
    except Exception as e:
        print(f"AI Emotion Detection Error: {e}")
        
    return None

def generate_insight(emotion: str, confidence: int, time_of_day: str = "day") -> dict:
    """
    Generates a short emotional summary and a 2-3 sentence, first-person-friendly explanation of what this mood snapshot might reflect.
    """
    fallback_result = {
        "summary": f"Feeling {emotion.lower()}",
        "insight": f"It looks like you're feeling {emotion.lower()} right now. Taking a moment to check in with yourself is a great step."
    }
    
    client = get_ai_client()
    if not client:
        return fallback_insight

    prompt = (
        f"The user's scan detected the emotion '{emotion}' with {confidence}% confidence. "
        f"The current time is roughly '{time_of_day}'.\n\n"
        "Task: Generate two things:\n"
        "1. A 'summary': A very brief (2-5 words) uplifting summary of their emotional state.\n"
        "2. An 'insight': A 2-3 sentence, first-person-friendly explanation of what this mood "
        "snapshot might reflect (e.g., 'It looks like you might be feeling...').\n"
        "Rules:\n"
        "- Do NOT diagnose.\n"
        "- Do NOT assume causes outside the given data.\n"
        "- NEVER use definitive phrasing like 'you have' or 'you need to'.\n"
        "- ALWAYS use softer framing like 'might', 'could', or 'seems like'."
    )
    
    class InsightResponse(BaseModel):
        summary: str
        insight: str
    
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash-lite',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PREAMBLE,
                temperature=0.7,
                response_mime_type="application/json",
                response_schema=InsightResponse,
            ),
        )
        if response.text:
            data = json.loads(response.text)
            return {
                "summary": data.get("summary", fallback_result["summary"]),
                "insight": data.get("insight", fallback_result["insight"])
            }
    except Exception as e:
        print(f"AI Generation Error: {e}")
        
    return fallback_result

def generate_suggestions(emotion: str, mood_score: int, time_of_day: str, base_suggestions: list[dict]) -> list[dict]:
    """
    Rephrases the base suggestion text in a warm, personalized tone without changing the underlying action.
    Returns a list of dictionaries with the original 'id' and the new 'text'.
    """
    fallback = [{"id": s.get("id"), "text": s.get("base_text")} for s in base_suggestions]
    
    client = get_ai_client()
    if not client:
        return fallback

    # We use a Pydantic schema for Gemini structured output
    class PersonalizedSuggestion(BaseModel):
        id: str
        text: str
        
    class SuggestionResponse(BaseModel):
        suggestions: list[PersonalizedSuggestion]

    prompt = (
        f"Context: The user is feeling '{emotion}' with a mood score of {mood_score}/100. "
        f"The time of day is '{time_of_day}'.\n\n"
        "Task: Rephrase the following wellness suggestions in a warm, personalized tone "
        "WITHOUT changing the underlying action. Keep them short and actionable.\n\n"
        "Suggestions:\n"
    )
    
    for s in base_suggestions:
        prompt += f"- ID: {s.get('id')} | Action: {s.get('base_text')}\n"

    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash-lite',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PREAMBLE,
                temperature=0.6,
                response_mime_type="application/json",
                response_schema=SuggestionResponse,
            ),
        )
        
        if response.text:
            data = json.loads(response.text)
            return data.get("suggestions", fallback)
    except Exception as e:
        print(f"AI Suggestions Error: {e}")
        
    return fallback
