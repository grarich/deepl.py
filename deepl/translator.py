from typing import List

from .adapter import Adapter
from .enums import Formality
from .enums import PreserveFormatting as PF
from .enums import SourceLang as SL
from .enums import SplitSentences as SS
from .enums import TargetLang as TL

__all__ = ['Translator']


class Translator:
    def __init__(self, adapter: Adapter) -> None:
        self._adapter = adapter

    def translate(self, text, *, target_lang: TL,
                  source_lang: SL = None, split_sentences: SS = None,
                  preserve_formatting: PF = None, formality: Formality = None) -> str:
        payload = {
            'text': text,
            'target_lang': target_lang.value
        }
        if source_lang:
            payload['source_lang'] = source_lang.value
        if split_sentences:
            payload['split_sentences'] = split_sentences.value
        if preserve_formatting:
            payload['preserve_formatting'] = preserve_formatting.value
        if formality:
            payload['formality'] = formality.value
        return self._adapter.get_translated_text(payload)

    def translate_multi(self, text_list: list, *, target_lang: TL,
                        source_lang: SL = None, split_sentences: SS = None,
                        preserve_formatting: PF = None, formality: Formality = None) -> List[str]:
        payload = {
            'text': text_list,
            'target_lang': target_lang.value
        }
        if source_lang:
            payload['source_lang'] = source_lang.value
        if split_sentences:
            payload['split_sentences'] = split_sentences.value
        if preserve_formatting:
            payload['preserve_formatting'] = preserve_formatting.value
        if formality:
            payload['formality'] = formality.value
        return self._adapter.get_translated_text_multi(payload)

    def usage(self) -> dict:
        return self._adapter.get_usage()

    def supported_languages(self) -> List[dict]:
        return self._adapter.get_supported_languages()
