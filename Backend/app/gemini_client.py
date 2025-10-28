import requests

# Replace with your actual Gemini API key
API_KEY = "AIzaSyAANZTUdJRXgdcmhjWZDbWIxXgo5MhIksY"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

def summarize_text(text: str) -> str:
    """
    Summarize the text using Gemini API
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {"parts": [{"text": f"Summarize the following text in 3-5 bullet points:\n{text[:8000]}"}]}
        ]
    }

    try:
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        summary = result["candidates"][0]["content"]["parts"][0]["text"]
        return summary
    except Exception as e:
        return f"Error while summarizing: {str(e)}"


def answer_question(chunks, question: str) -> str:
    """
    Answer a question using the provided document chunks
    """
    context = "\n".join(chunks[:5])  # take first few chunks
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {"parts": [{"text": f"Using the following context, answer the question:\nContext:\n{context}\nQuestion: {question}"}]}
        ]
    }

    try:
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        answer = result["candidates"][0]["content"]["parts"][0]["text"]
        return answer
    except Exception as e:
        return f"Error while generating answer: {str(e)}"
