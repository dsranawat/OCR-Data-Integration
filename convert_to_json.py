import os
import json
import re

text_folder = "."

text_files = [f for f in os.listdir(text_folder) if f.startswith("output_") and f.endswith(".txt")]

def extract_data(text):
    data = {}
    name_match = re.search(r"Patient Name\s*:\s*(.+)", text)
    dob_match = re.search(r"DOB\s*:\s*(\d{2}/\d{2}/\d{4})", text)
    
    data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
    data["dob"] = dob_match.group(1).strip() if dob_match else "Unknown"
    injection_match = re.search(r"INJECTION\s*:\s*(YES|NO)", text)
    exercise_match = re.search(r"Exercise Therapy\s*:\s*(YES|NO)", text)
    
    data["injection"] = injection_match.group(1) if injection_match else "Unknown"
    data["exercise_therapy"] = exercise_match.group(1) if exercise_match else "Unknown"
    difficulties = ["bending", "putting on shoes", "sleeping", "standing", "walking", "driving"]
    data["difficulty_ratings"] = {}
    for difficulty in difficulties:
        match = re.search(rf"{difficulty}:\s*(\d+)", text, re.IGNORECASE)
        data["difficulty_ratings"][difficulty] = int(match.group(1)) if match else 0
    symptoms = ["pain", "numbness", "tingling", "burning", "tightness"]
    data["pain_symptoms"] = {}
    for symptom in symptoms:
        match = re.search(rf"{symptom}:\s*(\d+)", text, re.IGNORECASE)
        data["pain_symptoms"][symptom] = int(match.group(1)) if match else 0

    data["medical_assistant_data"] = {
        "blood_pressure": re.search(r"Blood Pressure:\s*([\d/]+)", text).group(1) if re.search(r"Blood Pressure:\s*([\d/]+)", text) else "Unknown",
        "hr": int(re.search(r"HR:\s*(\d+)", text).group(1)) if re.search(r"HR:\s*(\d+)", text) else 0,
        "weight": int(re.search(r"Weight:\s*(\d+)", text).group(1)) if re.search(r"Weight:\s*(\d+)", text) else 0,
        "height": re.search(r"Height:\s*([\d.]+)", text).group(1) if re.search(r"Height:\s*([\d.]+)", text) else "Unknown",
        "spo2": int(re.search(r"SpO2:\s*(\d+)", text).group(1)) if re.search(r"SpO2:\s*(\d+)", text) else 0,
        "temperature": re.search(r"Temperature:\s*([\d.]+)", text).group(1) if re.search(r"Temperature:\s*([\d.]+)", text) else "Unknown",
        "blood_glucose": int(re.search(r"Blood Glucose:\s*(\d+)", text).group(1)) if re.search(r"Blood Glucose:\s*(\d+)", text) else 0,
        "respirations": int(re.search(r"Respirations:\s*(\d+)", text).group(1)) if re.search(r"Respirations:\s*(\d+)", text) else 0
    }

    return data

for text_file in text_files:
    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()
    structured_data = extract_data(text)
    json_filename = text_file.replace(".txt", ".json")
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(structured_data, json_file, indent=4)

    print(f"JSON file created: {json_filename}")

print("\nJSON conversion completed successfully.")
