import pytesseract
from PIL import Image

# Set the path to Tesseract-OCR (Ensure this is correct)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open the image (Fixed path issue)
image_path = r"C:\Users\user\OneDrive\Desktop\pharma-assistant\static\prescription.jpg"  # Update if needed
image = Image.open(image_path)

# Perform OCR
text = pytesseract.image_to_string(image)

# Print extracted text
print("Extracted Text:\n", text)
