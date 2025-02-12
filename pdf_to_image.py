from pdf2image import convert_from_path
import os
pdf_path = "Assesment.pdf"
output_folder = "images"
os.makedirs(output_folder, exist_ok=True)
images = convert_from_path(pdf_path, dpi=300)
image_paths = []
for i, img in enumerate(images):
    image_path = os.path.join(output_folder, f"page_{i+1}.jpg")
    img.save(image_path, "JPEG")
    image_paths.append(image_path)

print(f"PDF converted to images: {image_paths}")