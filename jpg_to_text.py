import cv2
import pytesseract
import os


image_folder = "images" # Folder containing images <input path in place of images>

image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".jpg")])

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    processed_path = os.path.join(image_folder, f"processed_{image_file}")
    cv2.imwrite(processed_path, gray)
    text = pytesseract.image_to_string(gray)
    print(f"\nExtracted text from {image_file}:\n")
    print(text)
    
    output_text_path = f"output_{image_file}.txt"
    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write(text)

print("\n OCR extraction completed. Check the text output in .txt files.")