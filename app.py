import streamlit as st
from chatbot import MedicalChatbot
from translator import Translator
import utils

st.set_page_config(page_title="Multilingual Medical Chatbot", layout="centered")

st.title("Multilingual Medical Support Chatbot")
st.markdown("A beginner-friendly, local-first medical chatbot demo. "
            "This project attempts to load a local Hugging Face model if available; "
            "otherwise it falls back to a safe rule-based responder.")

with st.sidebar:
    st.header("Settings")
    lang = st.selectbox("Interface language / Translate to:", ["auto", "en", "hi", "es", "fr", "bn", "ta", "te"])
    max_tokens = st.slider("Max response tokens (if using model)", 50, 512, 150)
    use_model = st.checkbox("Use local HF model (if installed)", value=False)
    st.markdown("⚠️ If you enable the model, make sure PyTorch and transformers are installed.")

if "history" not in st.session_state:
    st.session_state.history = []

translator = Translator()
bot = MedicalChatbot(use_model=use_model, max_tokens=max_tokens)

user_input = st.text_input("Enter your medical question (not for emergencies):", key="input")

if st.button("Send") and user_input.strip():
    # translate user input to English for model if needed
    if lang != "auto" and lang != "en":
        user_text_en = translator.translate_to_en(user_input, src=lang)
    else:
        # auto detect
        user_text_en = translator.translate_to_en(user_input)

    response_en = bot.get_response(user_text_en)

    # translate back to user's language if requested
    if lang != "auto" and lang != "en":
        response = translator.translate_from_en(response_en, dest=lang)
    else:
        response = response_en

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

    st.rerun()  # <-- FIXED (replaced experimental_rerun)

st.write("---")

for speaker, text in st.session_state.history[::-1]:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")

st.write("")
st.info("Disclaimer: This demo is for educational purposes only and not medical advice.")
st.markdown("### Helpful next steps")
st.markdown("- Run `pip install -r requirements.txt` (see README for PyTorch instructions).")
st.markdown("- Open terminal and run: `streamlit run app.py`")
