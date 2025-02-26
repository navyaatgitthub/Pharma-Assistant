import cv2
import pytesseract
import easyocr
from PIL import Image
import numpy as np

# ✅ Manually set the path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    """
    Preprocess the image for better OCR accuracy
    """
    # Load the image
    image = cv2.imread(image_path)

    # Resize the image to enhance recognition
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to enhance text
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 31, 2)

    # Remove noise using morphological operations
    kernel = np.ones((1, 1), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return cleaned

def extract_text_tesseract(image_path):
    """
    Extract printed text using Tesseract OCR
    """
    processed_image = preprocess_image(image_path)

    # Tesseract configuration for better recognition
    custom_config = r'--oem 3 --psm 6'

    extracted_text = pytesseract.image_to_string(processed_image, config=custom_config)

    return extracted_text

def extract_text_easyocr(image_path):
    """
    Extract handwritten text using EasyOCR
    """
    reader = easyocr.Reader(['en'])  # Load EasyOCR with English language
    result = reader.readtext(image_path)

    handwritten_text = " ".join([res[1] for res in result])  # Extract text from detected areas

    return handwritten_text

def extract_all_text(image_path):
    """
    Extract both printed and handwritten text from the image
    """
    printed_text = extract_text_tesseract(image_path)
    handwritten_text = extract_text_easyocr(image_path)

    return {
        'printed_text': printed_text,
        'handwritten_text': handwritten_text
    }

# ✅ Example usage
image_path = "path_to_your_prescription_image.jpg"
all_text = extract_all_text(image_path)

print("🔹 Printed Text:\n", all_text['printed_text'])
print("\n🔹 Handwritten Text:\n", all_text['handwritten_text'])
