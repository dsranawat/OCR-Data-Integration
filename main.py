import os
import subprocess
import sqlite3

# Database name
DB_NAME = "patients.db"

# Function to execute scripts
def run_script(script_name, args=[]):
    command = ["python", script_name] + args
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f" Error running {script_name}: {e}")

# Ensure database is set up before running any operations
if not os.path.exists(DB_NAME):
    print("\nSetting up database...\n")
    run_script("database.py")

# Step 1: Convert PDF to Images
pdf_path = input("\nEnter the PDF file path: ")
run_script("convert_pdf_to_images.py", [pdf_path])
print(" PDF converted to images successfully.")

# Step 2: Extract Text from Images (OCR)
image_folder = "images"
run_script("extract_text.py", [image_folder])
print(" Text extracted from images successfully.")

# Step 3: Convert Extracted Text to JSON
run_script("convert_to_json.py")
print(" Extracted text converted to JSON successfully.")

# Step 4: Store JSON Data in Database
run_script("insert_data.py")
print(" JSON data stored in the database successfully.")

print("\n All processes completed successfully. Exiting program.")
