# === 📁 LegalDocStruct-AI Full Code ===

# --- app.py ---
import streamlit as st
import os
import json
from utils.extract_text import extract_sectionwise_text
from utils.extract_tables import extract_tables_from_pdf
from utils.extract_images import extract_images_from_pdf
from utils.semantic_parser import analyze_document_structure

st.set_page_config(page_title="LegalDocStruct-AI", layout="wide")
st.title("📑 LegalDocStruct-AI — Extract Structure from Legal PDFs")

uploaded_file = st.file_uploader("Upload a Legal PDF Document", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ File uploaded successfully!")

    with st.spinner("Extracting..."):
        sections = extract_sectionwise_text("temp.pdf")
        tables = extract_tables_from_pdf("temp.pdf")
        image_paths = extract_images_from_pdf("temp.pdf")
        structure_json = analyze_document_structure(sections, tables, image_paths)

        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "structured.json"), "w") as f:
            json.dump(structure_json, f, indent=4)

    st.subheader("📌 Extracted Structure")
    st.json(structure_json)

    st.subheader("📷 Extracted Images")
    for img in image_paths:
        st.image(img, use_column_width=True)
