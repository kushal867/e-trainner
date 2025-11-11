from pdfminer.high_level import extract_text
import os

def extract_pdf_text(file_path):
    """
    Extracts text from a local PDF file.
    """
    if not os.path.exists(file_path):
        return ""
    try:
        text = extract_text(file_path)
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
