import cv2
import os
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess the image to improve OCR accuracy.
    - Converts to grayscale
    - Enhances contrast
    - Applies noise removal
    """
    # Ensure 'static' folder exists
    os.makedirs("static", exist_ok=True)

    # Load the image in grayscale mode
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Error: Could not load the image. Check the file path.")
        return None

    # Resize to standard size (optional but improves OCR)
    img = cv2.resize(img, (1000, 1200))

    # Apply adaptive histogram equalization for better contrast
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    img = clahe.apply(img)

    # Apply Otsu's thresholding to improve text contrast
    _, thresholded_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the preprocessed image
    preprocessed_image_path = "static/preprocessed.jpg"
    cv2.imwrite(preprocessed_image_path, thresholded_img)

    return preprocessed_image_path

# Run preprocessing
image_path = "static/prescription.jpg"  # Ensure prescription.jpg is inside 'static/'
preprocessed_path = preprocess_image(image_path)
print(f"Preprocessed image saved at: {preprocessed_path}")
