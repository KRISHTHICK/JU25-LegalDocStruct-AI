# --- utils/semantic_parser.py ---
def analyze_document_structure(sections, tables, image_paths):
    structured_data = {
        "sections": sections,
        "tables": tables,
        "images": image_paths
    }
    return structured_data
