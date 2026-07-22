import sys
import os

# Add the backend dir to sys.path so app module can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from deepface import DeepFace

print("DeepFace imported successfully!")
