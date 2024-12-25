import os
from deepface import DeepFace
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def analyze_attributes(image_path, actions=None):
    """
    Analyzes facial attributes such as emotion, age, gender, and race.
    """
    actions = actions or ["age", "gender", "emotion", "race"]
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image path is invalid: {image_path}")
        analysis = DeepFace.analyze(img_path=image_path, actions=actions)
        logging.info(f"Facial Attribute Analysis:\n{analysis}")
        return analysis
    except Exception as e:
        logging.error(f"Error during attribute analysis: {e}")
        return None

# Test the function
if __name__ == "__main__":
    # Path to the image
    test_image_path = "/content/r.jpg"  # Replace with the path to your test image
    
    # Analyze attributes
    result = analyze_attributes(test_image_path)
    if result:
        print("Facial Attribute Analysis Result:")
        print(json.dumps(result, indent=4))
