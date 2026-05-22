import streamlit as st

from utils.language_detector import detect_language
from utils.translator import (
    translate_to_english,
    translate_from_english
)

from utils.chatbot import generate_medical_response


# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Medical Support Chatbot",
    page_icon="🩺",
    layout="centered"
)


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.title("🩺 About Project")

    st.write("""
    This AI-powered multilingual chatbot can:
    
    ✅ Detect user language
    
    ✅ Translate to English
    
    ✅ Generate medical guidance
    
    ✅ Translate response back
    
    ✅ Support multilingual healthcare assistance
    """)

    st.subheader("Supported Languages")

    st.write("""
    • English
    
    • Tamil
    
    • Hindi
    
    • French
    
    • Spanish
    
    • German
    
    • Many more...
    """)

    st.info(
        "This project uses Hugging Face Transformers "
        "and Streamlit."
    )


# ---------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------

st.title("🩺 Multilingual Medical Support Chatbot")


# ---------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------

st.warning(
    "⚠️ Disclaimer: This chatbot is for educational "
    "purposes only and NOT a substitute for "
    "professional medical advice."
)


# ---------------------------------------------------
# EXAMPLE QUESTIONS
# ---------------------------------------------------

st.subheader("💡 Example Questions")

st.write("""
• I have fever and headache

• What are symptoms of diabetes?

• How to reduce cold and cough?

• வயிற்று வலி என்ன காரணம்?

• मुझे बुखार है
""")


# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------

user_input = st.text_area(
    "Enter your medical question:",
    height=150
)


# ---------------------------------------------------
# RESPONSE BUTTON
# ---------------------------------------------------

if st.button("Get Response"):

    if user_input.strip() == "":

        st.error("Please enter a medical question.")

    else:

        try:

            with st.spinner("Generating medical response..."):

                # STEP 1
                detected_language = detect_language(user_input)

                # STEP 2
                english_text = translate_to_english(
                    user_input,
                    detected_language
                )

                # STEP 3
                medical_response = generate_medical_response(
                    english_text
                )

                # STEP 4
                final_response = translate_from_english(
                    medical_response,
                    detected_language
                )

            # ---------------------------------------------------
            # OUTPUT SECTION
            # ---------------------------------------------------

            st.success("Response Generated Successfully!")

            st.subheader("🌍 Detected Language")

            st.write(detected_language)

            st.subheader("🔤 Translated English Query")

            st.write(english_text)

            st.subheader("🤖 Chatbot Response")

            st.write(final_response)

        except Exception as error:

            st.error(
                f"An error occurred: {error}"
            )