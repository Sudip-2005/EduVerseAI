import requests

API_KEY = "AIzaSyAANZTUdJRXgdcmhjWZDbWIxXgo5MhIksY"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

def summarize_text_with_gemini(text: str) -> str:
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": f"Summarize the following text in 3-5 bullet points:\n{text}"}
                ]
            }
        ]
    }

    try:
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        # Gemini responses are structured like this:
        summary = result["candidates"][0]["content"]["parts"][0]["text"]
        return summary
    except Exception as e:
        return f"Error while summarizing: {str(e)}"
