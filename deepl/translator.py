from typing import List

from .adapter import Adapter

__all__ = ['Translator']


class Translator:
    def __init__(self, adapter: Adapter) -> None:
        self._adapter = adapter

    def translate(self, text, *, target_lang,
                  source_lang=None, split_sentences=None,
                  preserve_formatting=None, formality=None) -> str:
        payload = {
            'text': text,
            'target_lang': str(target_lang)
        }
        if source_lang:
            payload['source_lang'] = str(source_lang)
        if split_sentences:
            payload['split_sentences'] = str(split_sentences)
        if preserve_formatting:
            payload['preserve_formatting'] = str(preserve_formatting)
        if formality:
            payload['formality'] = str(formality)
        return self._adapter.get_translated_text(payload)

    def translate_multi(self, text_list: list, *, target_lang,
                        source_lang=None, split_sentences=None,
                        preserve_formatting=None, formality=None) -> List[str]:
        payload = {
            'text': text_list,
            'target_lang': str(target_lang)
        }
        if source_lang:
            payload['source_lang'] = str(source_lang)
        if split_sentences:
            payload['split_sentences'] = str(split_sentences)
        if preserve_formatting:
            payload['preserve_formatting'] = str(preserve_formatting)
        if formality:
            payload['formality'] = str(formality)
        return self._adapter.get_translated_text_multi(payload)

    def usage(self) -> dict:
        return self._adapter.get_usage()

    def supported_languages(self) -> List[dict]:
        return self._adapter.get_supported_languages()
