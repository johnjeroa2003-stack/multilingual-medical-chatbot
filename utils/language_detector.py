from langdetect import detect

def detect_language(text):

    try:
        language = detect(text)

        # Force English for normal English sentences
        if language not in ["ta", "hi", "fr", "es", "de"]:
            return "en"

        return language

    except Exception:
        return "en"