import torch
import torchvision.transforms as transforms
from PIL import Image
import cv2
import numpy as np
import pytesseract
from onnxruntime import InferenceSession
from sklearn.preprocessing import StandardScaler
import joblib  # For saving and loading models

# Configure Tesseract path (update if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to extract text from prescription images
def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    extracted_text = pytesseract.image_to_string(thresh)
    return extracted_text.strip()

# Load pre-trained ONNX model for disease detection
onnx_model_path = "disease_model.onnx"
onnx_session = InferenceSession(onnx_model_path)

def analyze_medical_image(image_path):
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    img_tensor = transform(image).unsqueeze(0)

    # Convert to numpy for ONNX
    input_data = img_tensor.numpy()
    outputs = onnx_session.run(None, {"input": input_data})
    
    # Get prediction label
    predicted_label = np.argmax(outputs[0])
    return f"Diagnosis: {predicted_label}"

# Function to predict disease based on symptoms
def predict_disease(symptoms):
    model = joblib.load("disease_prediction_model.pkl")
    symptoms_vector = np.array(symptoms).reshape(1, -1)
    prediction = model.predict(symptoms_vector)
    return prediction[0]
