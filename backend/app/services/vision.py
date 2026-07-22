import base64
import numpy as np
import cv2
import mediapipe as mp
import os
from app.services.ai import detect_emotion_vision

try:
    mp_face_detection = mp.solutions.face_detection
    # Initialize the face detection model with a standard confidence threshold
    face_detector = mp_face_detection.FaceDetection(min_detection_confidence=0.7)
    HAS_MEDIAPIPE = True
except (ImportError, AttributeError):
    HAS_MEDIAPIPE = False
    print("WARNING: mediapipe module not found or incompatible. Using mock face detection.")

class VisionError(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(self.message)

def decode_base64_image(base64_string: str) -> np.ndarray:
    try:
        # Strip the data:image... header if present
        if "base64," in base64_string:
            base64_string = base64_string.split("base64,")[1]
            
        img_data = base64.b64decode(base64_string)
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Failed to decode image")
        return img
    except Exception as e:
        raise VisionError("INVALID_IMAGE", "We couldn't process the image provided.")



def analyze_image(base64_string: str) -> dict:
    """
    Analyzes an image to detect a single face, determine its dominant emotion via Gemini Vision,
    and calculate a mood score.
    """
    img = decode_base64_image(base64_string)
    


    # MediaPipe expects RGB images
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    try:
        if HAS_MEDIAPIPE:
            results = face_detector.process(img_rgb)
            
            if not results.detections:
                raise VisionError(
                    "NO_FACE_DETECTED", 
                    "We couldn't quite see your face — try moving a little closer to good light."
                )
                
            if len(results.detections) > 1:
                raise VisionError(
                    "MULTIPLE_FACES_DETECTED",
                    "We detected multiple faces. Please ensure only your face is in the frame and try again."
                )
                
            detection = results.detections[0]
            confidence = int(detection.score[0] * 100)
            
            if confidence < 75:
                raise VisionError(
                    "LOW_CONFIDENCE",
                    "The image isn't clear enough. Please try again with better lighting and ensure your face is centered."
                )
            
            h, w, _ = img.shape
            bbox = detection.location_data.relative_bounding_box
            
            # Add a slight margin (10%) around the face for context
            margin_x = bbox.width * 0.1
            margin_y = bbox.height * 0.1
            
            x1 = max(0, int((bbox.xmin - margin_x) * w))
            y1 = max(0, int((bbox.ymin - margin_y) * h))
            x2 = min(w, int((bbox.xmin + bbox.width + margin_x) * w))
            y2 = min(h, int((bbox.ymin + bbox.height + margin_y) * h))
            
            face_img = img[y1:y2, x1:x2]
            
            if face_img.size == 0:
                raise VisionError(
                    "INVALID_FACE_CROP", 
                    "We couldn't correctly isolate your face. Please center your face in the frame and try again."
                )
        else:
            confidence = 95
            face_img = img
            
        # Encode cropped face back to base64 for Gemini
        _, buffer = cv2.imencode('.jpg', face_img, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
        face_base64 = base64.b64encode(buffer).decode('utf-8')
        
        # Request Gemini Vision Analysis
        ai_result = detect_emotion_vision(face_base64, mime_type="image/jpeg")
        
        if not ai_result:
            raise VisionError(
                "ANALYSIS_FAILED",
                "Our AI was unable to confidently determine your emotion. Please try again."
            )
            
        dominant_emotion = ai_result.emotion
        emotion_confidence = ai_result.confidence
        
        if emotion_confidence < 60:
             raise VisionError(
                "LOW_EMOTION_CONFIDENCE",
                "Unable to confidently determine your mood. Please try scanning again with better lighting or a clearer expression."
            )

        emotion_scores = {
            'Happy': 90,
            'Surprise': 70,
            'Calm': 60,
            'Relaxed': 60,
            'Neutral': 50,
            'Sad': 30,
            'Anxious': 30,
            'Fear': 20,
            'Angry': 10,
            'Disgust': 10
        }
        
        base_score = emotion_scores.get(dominant_emotion, 50)
        # Add slight variation based on confidence
        mood_score = min(100, max(0, base_score + (emotion_confidence % 10) - 5))
        
        # Simulate probabilities for the frontend pie charts
        emotion_probs = {e: 5.0 for e in emotion_scores.keys()}
        emotion_probs[dominant_emotion] = 80.0
        
        return {
            "emotion": dominant_emotion,
            "confidence": emotion_confidence,
            "moodScore": mood_score,
            "emotion_probabilities": emotion_probs
        }
        
    except VisionError:
        raise
    except Exception as e:
        print(f"Vision analysis failed: {e}")
        raise VisionError(
            "ANALYSIS_FAILED",
            "We encountered an issue analyzing your expression. Please try again."
        )
