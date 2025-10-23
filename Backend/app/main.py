from fastapi import FastAPI, UploadFile, File
import shutil
import os

from .extract import extract_text_from_pdf
from .gemini_client import summarize_text_with_gemini

app = FastAPI(title="EduIntelli Backend")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Backend is working!"}

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text_from_pdf(file_path)

    # Summarize using Gemini
    summary = summarize_text_with_gemini(text)

    return {"summary": summary}
