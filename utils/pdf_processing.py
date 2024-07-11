from fastapi import UploadFile
from PyPDF2 import PdfReader

def preprocess_pdf(file: UploadFile):
    reader = PdfReader(file.file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text