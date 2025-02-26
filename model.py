import cv2
import pytesseract
import numpy as np

# Configure Tesseract path (for Windows, update the path accordingly)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    # Read image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to remove noise
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Use OCR to extract text
    extracted_text = pytesseract.image_to_string(thresh)

    return extracted_text.strip()
