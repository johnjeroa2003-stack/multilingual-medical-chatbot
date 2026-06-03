from langdetect import detect

def detect_language(text):

    try:
        language = detect(text)

        supported_languages = [
            "en", "ta", "hi", "fr", "es", "de"
        ]

        if language not in supported_languages:
            return "en"

        return language

    except Exception:
        return "en"