import cv2
import pytesseract

def preprocess_image(image_path):
    """ Preprocess image to improve OCR accuracy """
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply adaptive thresholding to improve text visibility
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    return thresh

def extract_printed_text(image_path):
    """ Extract printed text using Tesseract OCR """
    processed_image = preprocess_image(image_path)
    
    # Use Tesseract OCR
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(processed_image, config=custom_config)
    
    return text

if __name__ == "__main__":
    image_path = r"C:\Users\user\OneDrive\Desktop\pharma-assistant\static\prescription.jpg"
    
    # Extract printed text
    printed_text = extract_printed_text(image_path)
    
    # Save the extracted text to a file for later processing
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(printed_text)
    
    print("\nExtracted Printed Text:\n", printed_text)
