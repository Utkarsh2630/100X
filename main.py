import streamlit as st
from openai import OpenAI
import tempfile
import os
import hashlib
from dotenv import load_dotenv

# -------------------- SETUP --------------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are Utkarsh Kumar, an IIT ISM Dhanbad graduate applying to 100x's AI Agent Team.
Answer interview questions authentically and concisely as you would. Be confident, genuine, and professional.
Focus on: AI/ML expertise, problem-solving skills, remote work capability, and growth mindset.
IMPORTANT: Always respond in English. Do not use any other language. Note that you are not expert in Machine Learning, stay on Gen AI only."""

st.set_page_config(page_title="AI Interview Voice Bot", page_icon="🎙️", layout="centered")

# -------------------- SESSION STATE --------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Hi! Tap the mic button below and ask me an interview question."}
    ]

if "last_audio_hash" not in st.session_state:
    st.session_state.last_audio_hash = None

if "turn_id" not in st.session_state:
    st.session_state.turn_id = 0

if "last_assistant_audio" not in st.session_state:
    st.session_state.last_assistant_audio = None

# -------------------- HEADER --------------------
st.title("🎙️ AI Interview Voice Bot")
st.caption("Utkarsh Kumar • IIT ISM Dhanbad")

# -------------------- CHAT HISTORY --------------------
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------- LAST BOT AUDIO (ALWAYS VISIBLE) --------------------
if st.session_state.last_assistant_audio is not None:
    st.audio(st.session_state.last_assistant_audio, format="audio/mp3")

# -------------------- MIC INPUT --------------------
st.markdown("---")
st.caption("🎤 Tap mic → speak → stop → bot replies")

audio_value = st.audio_input(
    "Record your question",
    key=f"mic_{st.session_state.turn_id}",
    label_visibility="collapsed"
)

if audio_value:
    try:
        audio_bytes = audio_value.read()
        audio_hash = hashlib.md5(audio_bytes).hexdigest()

        # prevent duplicate processing on rerun
        if audio_hash == st.session_state.last_audio_hash:
            st.stop()

        st.session_state.last_audio_hash = audio_hash

        # ----------- TRANSCRIBE -----------
        with st.spinner("Listening & transcribing..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
                f.write(audio_bytes)
                temp_audio_path = f.name

            with open(temp_audio_path, "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language="en"
                )

            user_text = transcript.text.strip()

            try:
                os.remove(temp_audio_path)
            except:
                pass

        if not user_text:
            st.stop()

        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_text})

        # ----------- STREAM TEXT RESPONSE -----------
        assistant_container = st.chat_message("assistant")
        text_placeholder = assistant_container.empty()

        full_answer = ""

        with st.spinner("Thinking..."):
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
                stream=True
            )

            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    full_answer += delta
                    text_placeholder.markdown(full_answer)

        full_answer = full_answer.strip()

        # Save assistant text
        st.session_state.messages.append({"role": "assistant", "content": full_answer})

        # ----------- GENERATE VOICE AFTER TEXT IS DONE -----------
        with assistant_container:
            voice_placeholder = st.empty()
            with voice_placeholder:
                with st.spinner("Generating voice reply..."):
                    speech = client.audio.speech.create(
                        model="tts-1",
                        voice="alloy",
                        input=full_answer
                    )
                    st.session_state.last_assistant_audio = speech.content

            st.audio(st.session_state.last_assistant_audio, format="audio/mp3")

        # Reset mic widget for next question
        st.session_state.turn_id += 1
        st.rerun()

    except Exception as e:
        st.error(f"Error: {str(e)}")
