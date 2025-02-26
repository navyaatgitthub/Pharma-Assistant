import random

# Mock disease prediction model
def predict_disease(symptoms):
    symptom_list = symptoms.lower().split(",")  # Convert to lowercase and split
    possible_diseases = {
        "fever,cough": "Flu",
        "headache,nausea": "Migraine",
        "fatigue,weight loss": "Diabetes"
    }

    for key in possible_diseases:
        if all(symptom in symptom_list for symptom in key.split(",")):
            return possible_diseases[key]

    return random.choice(["Common Cold", "Malaria", "Unknown Condition"])

if __name__ == "__main__":
    print("📢 Disease Prediction System Started!")
    
    user_input = input("Enter symptoms separated by commas (e.g., fever,cough): ")
    predicted_disease = predict_disease(user_input)
    
    print(f"🩺 Predicted Disease: {predicted_disease}")
