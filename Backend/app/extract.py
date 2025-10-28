from io import BytesIO
from PyPDF2 import PdfReader
from fastapi import UploadFile

def extract_text_from_pdf(file: UploadFile) -> str:
    """
    Extract text from an UploadFile object
    """
    # Read PDF bytes
    pdf_bytes = file.file.read()
    pdf_stream = BytesIO(pdf_bytes)
    reader = PdfReader(pdf_stream)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text
