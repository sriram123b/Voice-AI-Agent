import streamlit as st
import whisper
from tools import create_file, write_code, summarize_text
import os

model = whisper.load_model("base")

st.title(" Voice AI Agent")

audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if audio_file:
    file_path = "temp.wav"
    
    with open(file_path, "wb") as f:
        f.write(audio_file.read())

    # ✅ Speech-to-Text
    result = model.transcribe(file_path)
    text = result["text"]

    st.write("### 📝 Transcription")
    st.write(text)

    # ✅ Intent detection (NO API)
    text_lower = text.lower()

    if "create file" in text_lower:
        intent = "create_file"
    elif "write code" in text_lower or "python" in text_lower:
        intent = "write_code"
    elif "summarize" in text_lower:
        intent = "summarize"
    else:
        intent = "chat"

    st.write("### 🧠 Intent")
    st.write(intent)

    # ✅ Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # ✅ Tool execution
    if intent == "create_file":
        output = create_file("sample.txt")

    elif intent == "write_code":
        code = "# Auto-generated code\nprint('Hello from AI Agent')"
        output = write_code("code.py", code)

    elif intent == "summarize":
        output = summarize_text(text)

    else:
        output = "Chat response not implemented (MVP)"

    st.write("### ⚙️ Action")
    st.success(output)