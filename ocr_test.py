from PIL import Image
import pytesseract

# Set the correct Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open the image file
image = Image.open("sample_text.png")

# Perform OCR (extract text from the image)
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)
