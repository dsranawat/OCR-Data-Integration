import sqlite3
import json
import os

# Database name
DB_NAME = "patients.db"

# Connect to SQLite database (or create it)
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create 'patients' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dob TEXT
)
""")

# Create 'forms_data' table to store JSON
cursor.execute("""
CREATE TABLE IF NOT EXISTS forms_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    form_json TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
)
""")

conn.commit()
conn.close()

print("Database setup completed.")
