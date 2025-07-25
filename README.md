# JU25-LegalDocStruct-AI
GEN AI

LegalDocStruct-AI: Intelligent Structuring of Legal Documents
🧠 Idea:
Many legal documents like contracts, agreements, or policy papers come in unstructured formats (PDFs, scanned images). This project intelligently extracts and structures the following elements:

Section-wise Text

Tables

Images/Diagrams

Legal Entities (e.g., party names, dates, obligations)

Output stored in structured JSON and folders.

📌 Problem it Solves:
Manual review and structuring of legal documents is slow and error-prone. LegalDocStruct-AI automates the understanding of content, enabling:

Faster search

Legal clause comparison

Automated compliance check

Document indexing

🛠️ Tech Stack:
Python

Streamlit – for UI

PyMuPDF / pdfplumber – for text and table extraction

Pillow / pdf2image – for image extraction

spaCy / LLM – for entity detection

Tesseract – for OCR (optional)

📂 Folder Structure:
bash
Copy
Edit
legaldocstruct-ai/
├── app.py                   # Streamlit UI
├── utils/
│   ├── extract_text.py      # Section-wise text extraction
│   ├── extract_tables.py    # Extract tables with structure
│   ├── extract_images.py    # Save diagrams/figures
│   ├── extract_entities.py  # Extract legal entities
├── output/
│   ├── structured.json
│   └── images/
├── samples/
│   └── sample_nda.pdf       # Sample test legal document
└── requirements.txt
✅ Output:
structured.json:

json
Copy
Edit
{
  "sections": {
    "1. Definitions": "...",
    "2. Obligations": "..."
  },
  "tables": [
    {"page": 2, "table": [["Party", "Obligation"], ["X Corp", "Deliver by June 2025"]]}
  ],
  "images": ["page3_diagram1.png"],
  "legal_entities": {
    "parties": ["X Corp", "Y Corp"],
    "dates": ["June 1, 2025"],
    "clauses": ["Confidentiality", "Indemnification"]
  }
}
