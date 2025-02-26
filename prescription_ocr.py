import pytesseract
import cv2

# Load prescription image
image_path = r"C:\Users\user\OneDrive\Desktop\pharma-assistant\static\prescription.jpg"
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply OCR
extracted_text = pytesseract.image_to_string(gray)

# Save extracted text
text_output_path = r"C:\Users\user\OneDrive\Desktop\pharma-assistant\static\extracted_text.txt"
with open(text_output_path, "w") as text_file:
    text_file.write(extracted_text)

print(f"📜 Extracted text saved at: {text_output_path}")
