from deep_translator import GoogleTranslator

def translate_to_english(text, source_language):
    """
    Translates any language text into English.
    """

    translated_text = GoogleTranslator(
        source=source_language,
        target='en'
    ).translate(text)

    return translated_text


def translate_from_english(text, target_language):
    """
    Translates English text back to user's language.
    """

    translated_text = GoogleTranslator(
        source='en',
        target=target_language
    ).translate(text)

    return translated_text