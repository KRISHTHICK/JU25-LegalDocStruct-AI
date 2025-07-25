# --- utils/extract_images.py ---
import fitz
import os

def extract_images_from_pdf(pdf_path, output_folder="output/images"):
    os.makedirs(output_folder, exist_ok=True)
    doc = fitz.open(pdf_path)
    image_paths = []

    for i in range(len(doc)):
        for img_index, img in enumerate(doc.get_page_images(i)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            image_path = os.path.join(output_folder, f"page_{i+1}_img_{img_index}.{ext}")
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            image_paths.append(image_path)

    return image_paths
