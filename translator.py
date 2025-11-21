# Lightweight translator wrapper. Tries googletrans first; else provides passthrough.
try:
    from googletrans import Translator as _GoogleTranslator
    _GT_AVAILABLE = True
except Exception:
    _GT_AVAILABLE = False

class Translator:
    def __init__(self):
        if _GT_AVAILABLE:
            self.gt = _GoogleTranslator()
        else:
            self.gt = None

    def translate_to_en(self, text: str, src: str = 'auto') -> str:
        if not text:
            return text
        if self.gt:
            try:
                res = self.gt.translate(text, src=src, dest='en')
                return res.text
            except Exception as e:
                print('googletrans failed:', e)
        # fallback: return original
        return text

    def translate_from_en(self, text: str, dest: str = 'en') -> str:
        if not text:
            return text
        if dest == 'en' or dest == 'auto':
            return text
        if self.gt:
            try:
                res = self.gt.translate(text, src='en', dest=dest)
                return res.text
            except Exception as e:
                print('googletrans failed:', e)
        return text
