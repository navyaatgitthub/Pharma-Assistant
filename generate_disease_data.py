import pandas as pd
import random

# Define symptoms
symptoms = ["Fever", "Cough", "Fatigue", "Headache", "Sore Throat"]
diseases = ["Flu", "Covid-19", "Dengue", "Tonsillitis", "Allergy"]

# Generate random data
data = []
for _ in range(100):  # Generate 100 rows
    row = [random.choice([0, 1]) for _ in symptoms]  # Random symptoms (0 or 1)
    row.append(random.choice(diseases))  # Random disease
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=symptoms + ["Diagnosis"])

# Save as CSV
df.to_csv("disease_data.csv", index=False)

print("✅ Random dataset 'disease_data.csv' created successfully!")
