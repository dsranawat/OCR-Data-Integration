OCR Patient Assessment Data Extraction

Overview
This project extracts patient assessment data from scanned forms using OCR, structures it into JSON, and stores it in a SQL database.

Project Structure
- pdf_to_image.py → Converts PDF to images.
- jpg_to_text.py → Extracts text using OCR.
- convert_to_json.py → Converts extracted text to structured JSON.
- database.py → Sets up SQLite database.
- main.py → Automates the entire workflow.

Installation & Setup
1. Install Dependencies
      pip install -r requirements.txt
2.Run the Main Script
      python main.py
