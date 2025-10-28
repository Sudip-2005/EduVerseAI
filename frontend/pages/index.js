import { useState } from "react";
import axios from "axios";

export default function Home() {
const [file, setFile] = useState(null);
const [filename, setFilename] = useState("");
const [summary, setSummary] = useState("");
const [question, setQuestion] = useState("");
const [answer, setAnswer] = useState("");

const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://127.0.0.1:8000/upload/", formData);
    setFilename(res.data.filename);
    setSummary(res.data.summary);
};

const handleAsk = async () => {
    if (!question || !filename) return;

    const formData = new FormData();
    formData.append("filename", filename);
    formData.append("question", question);

    const res = await axios.post("http://127.0.0.1:8000/chat/", formData);
    setAnswer(res.data.answer);
};

return (
    <div style={{ padding: "20px" }}>
    <h1>EduIntelli – PDF Chat</h1>

    <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
    />
    <button onClick={handleUpload}>Upload & Summarize</button>

    <h2>Summary:</h2>
    <p>{summary}</p>
    <hr />

    <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a question"
        style={{ width: "300px" }}
    />
    <button onClick={handleAsk}>Ask</button>

    <h2>Answer:</h2>
    <p>{answer}</p>
    </div>
);
}
