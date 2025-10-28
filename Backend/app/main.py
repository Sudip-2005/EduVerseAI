from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from app.extract import extract_text_from_pdf
from app.gemini_client import summarize_text, answer_question

app = FastAPI()

# Allow frontend to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary in-memory storage for uploaded documents
documents = {}

@app.post("/upload/")
async def upload_file(file: UploadFile):
    """
    Upload a PDF, extract text, split into chunks, and generate a summary.
    """
    # Extract text from PDF
    text = extract_text_from_pdf(file)

    # Split text into 1000-character chunks for chat
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    documents[file.filename] = chunks

    # Generate summary using Gemini API
    summary = summarize_text(text)

    return {"filename": file.filename, "summary": summary}


@app.post("/chat/")
async def chat_with_doc(filename: str = Form(...), question: str = Form(...)):
    """
    Ask a question about an uploaded document.
    """
    if filename not in documents:
        return {"error": "Document not found. Upload it first."}

    # Use first few chunks as context
    text_chunks = documents[filename]

    # Generate answer
    answer = answer_question(text_chunks, question)

    return {"answer": answer}
