🚀 Pharma Assistant – AI-powered Prescription & Diagnostic Tool
A smart AI-based system that extracts text from handwritten prescriptions, analyzes medical images, and assists in disease diagnosis. Built using Python, OpenCV, Tesseract, and Flask.

📌 Features
✅ Handwritten prescription text extraction using OCR
✅ AI-powered medical image analysis
✅ Disease prediction with treatment suggestions
✅ User-friendly interface with Flask web app
✅ Integration of AI models for enhanced accuracy

🛠️ Tech Stack
Programming Language: Python
Libraries Used: OpenCV, Tesseract OCR, Flask, TensorFlow/PyTorch
Framework: Flask for web deployment
🚀 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd pharma-assistant
2️⃣ Set Up the Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy
Edit
python app.py
The Flask app will run on http://127.0.0.1:5000/.

📜 Usage
1️⃣ Upload a prescription image.
2️⃣ Extract handwritten text using OCR.
3️⃣ Analyze medical images for disease prediction.
4️⃣ Get treatment suggestions.

📂 Project Structure
php
Copy
Edit
pharma-assistant/
│── static/              # Stores images & assets  
│── templates/           # HTML templates for Flask  
│── app.py               # Main Flask application  
│── extract_prescription.py  # OCR-based text extraction  
│── disease_classifier.py    # AI model for disease prediction  
│── requirements.txt     # List of dependencies  
│── README.md            # Project documentation  
🤖 Future Enhancements
🔹 Improve OCR accuracy with advanced preprocessing
🔹 Deploy as a cloud-based API
🔹 Integrate voice-based prescription analysis
