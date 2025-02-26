import json

# Load structured prescription data
json_path = "C:\\Users\\user\\OneDrive\\Desktop\\pharma-assistant\\static\\prescription_data.json"

with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Print extracted prescription details
print("\n📜 Extracted Prescription Details:\n")
for key, value in data.items():
    print(f"{key.replace('_', ' ').capitalize()}: {value}")
