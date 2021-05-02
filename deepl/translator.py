from .adapter import Adapter


class Translator:
    def __init__(self, adapter: Adapter):
        self._adapter = adapter

    def translate(self, text, target_lang, *, source_lang=None, split_sentences=None, preserve_formatting=None, formality=None):
        payload = {
            'text': text,
            'target_lang': str(target_lang)
        }
        if source_lang:
            payload['source_lang'] = str(source_lang)
        if split_sentences:
            payload['split_sentences'] = split_sentences
        if preserve_formatting:
            payload['preserve_formatting'] = preserve_formatting
        if formality:
            payload['formality'] = str(formality)
        return self._adapter.get_translated_text(payload)

    def usage(self):
        return self._adapter.get_usage()

    def supported_languages(self):
        return self._adapter.get_supported_languages()

