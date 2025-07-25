# === Streamlit App: app.py ===
import streamlit as st
import json
from utils.extract_text import extract_sections_from_pdf
from utils.extract_tables import extract_tables_from_pdf
from utils.extract_images import extract_images_from_pdf
from utils.extract_entities import extract_named_entities
import os

st.set_page_config(page_title="LegalDocStruct-AI", layout="wide")
st.title("📄 LegalDocStruct-AI: Structured Info Extractor from Legal Docs")

uploaded_file = st.file_uploader("Upload a Legal PDF Document", type=["pdf"])

if uploaded_file:
    # Save to a temporary location
    file_path = f"samples/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Section-wise text
    with st.spinner("Extracting Sections..."):
        sections = extract_sections_from_pdf(file_path)

    # Tables
    with st.spinner("Extracting Tables..."):
        tables = extract_tables_from_pdf(file_path)

    # Images
    with st.spinner("Extracting Images..."):
        image_paths = extract_images_from_pdf(file_path, output_folder="output/images")

    # Entities
    with st.spinner("Extracting Named Entities..."):
        entities = extract_named_entities(sections)

    # Structured output
    structured_output = {
        "file_name": uploaded_file.name,
        "sections": sections,
        "tables": tables,
        "images": image_paths,
        "entities": entities
    }

    with open("output/structured.json", "w") as f:
        json.dump(structured_output, f, indent=2)

    st.success("✅ Extraction Complete! View Results Below:")

    st.subheader("📑 Sections")
    for title, content in sections.items():
        st.markdown(f"### {title}")
        st.write(content[:500] + ("..." if len(content) > 500 else ""))

    st.subheader("📊 Extracted Tables")
    for i, table in enumerate(tables):
        st.markdown(f"#### Table {i+1}")
        st.dataframe(table)

    st.subheader("🖼️ Extracted Images")
    for path in image_paths:
        st.image(path, width=400)

    st.subheader("🔍 Named Entities")
    st.json(entities)
