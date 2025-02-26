import json

# Path to your JSON file
json_path = "C:\\Users\\user\\OneDrive\\Desktop\\pharma-assistant\\static\\prescription_data.json"

# Load and print the content of your JSON file
with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Print the whole JSON structure
print(json.dumps(data, indent=4))  # Pretty print the JSON
