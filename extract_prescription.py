import easyocr
import cv2
import os

# Suppress TensorFlow warnings
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

def preprocess_image(image_path):
    """ Preprocess image to improve OCR accuracy """
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"❌ ERROR: Could not read the image at {image_path}. Check the file path and format.")
        return None
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

def extract_handwritten_text(image_path):
    """ Extract handwritten text using EasyOCR """
    processed_image = preprocess_image(image_path)
    
    if processed_image is None:
        return "OCR Failed: Image could not be read."
    
    reader = easyocr.Reader(['en'])  # Initialize the reader for English
    result = reader.readtext(processed_image)  # Extract text from the image
    text = " ".join([word[1] for word in result])  # Combine all detected text
    return text

# Updated Image Path
image_path = r"C:\Users\user\OneDrive\Desktop\pharma-assistant\images\prescription2.jpg"

# Run OCR Extraction
handwritten_text = extract_handwritten_text(image_path)
print("✅ Extracted Handwritten Text:\n", handwritten_text)
