# Dummy dictionary for disease prediction
disease_data = {
    "fever cough headache": ("Flu", "Drink fluids, rest, and take paracetamol."),
    "fever rash joint pain": ("Dengue", "Consult a doctor, stay hydrated, and rest."),
    "chest pain breathlessness": ("Heart Disease", "Seek immediate medical help."),
    "cough difficulty breathing": ("COVID-19", "Isolate and consult a healthcare provider."),
}

def predict_disease(symptoms):
    symptoms = symptoms.lower().strip()  # Normalize input

    for key, value in disease_data.items():
        if all(word in symptoms for word in key.split()):
            return value  # (Disease, Treatment)

    return "Unknown Disease", "Consult a doctor for further diagnosis."

if __name__ == "__main__":
    print(predict_disease("fever cough headache"))  # Test function
