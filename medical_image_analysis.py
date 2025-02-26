import cv2
import numpy as np
from PIL import Image

def analyze_medical_image(image_path):
    """ Analyze the X-ray image and return a dummy diagnosis. """
    try:
        # Load image
        image = Image.open(image_path).convert("RGB")
        image_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Dummy processing: Check for bright areas (assume abnormality)
        avg_pixel_value = np.mean(image_cv)

        if avg_pixel_value > 100:
            return "🩺 Possible Bone Fracture Detected!"
        else:
            return "✅ No Abnormalities Detected."

    except Exception as e:
        return f"❌ Error processing image: {e}"

# Run the program
if __name__ == "__main__":
    print("📷 Enter medical image path: ")
    image_path = input().strip()

    # Call the function
    result = analyze_medical_image(image_path)

    print(result)
