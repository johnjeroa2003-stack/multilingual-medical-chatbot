from langdetect import detect

def detect_language(text):
    """
    Detects the language of the user input text.
    """

    try:
        language = detect(text)
        return language

    except Exception:
        return "en"