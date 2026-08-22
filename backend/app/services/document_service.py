import fitz  # PyMuPDF
from pathlib import Path


def extract_text_from_pdf(file_path: Path) -> str:
    """
    Extract all text from a PDF file.
    """

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text