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

    def upload_translation_file(self, file_path, *,
                                target_lang: TL, file_name: str = None, source_lang: SL = None,
                                split_sentences: SS = None, preserve_formatting: PF = None,
                                formality: Formality = None) -> dict:
        payload = {
            'target_lang': target_lang.value
        }
        if file_name:
            payload['file_name'] = file_name
        if source_lang:
            payload['source_lang'] = source_lang.value
        if split_sentences:
            payload['split_sentences'] = split_sentences.value
        if preserve_formatting:
            payload['preserve_formatting'] = preserve_formatting.value
        if formality:
            payload['formality'] = formality.value
        return self._adapter.upload_translation_file(payload, open(file_path, 'rb'))

    def check_translation_file(self, document_id: str, document_key: str) -> dict:
        payload = {
            'document_key': document_key
        }
        return self._adapter.check_translated_file_status(document_id, payload)

    def download_translated_file(self, document_id: str, document_key: str) -> bytes:
        payload = {
            'document_key': document_key
        }
        return self._adapter.download_translated_file(document_id, payload)

    def translate_xml(self, text, *, target_lang: TL,
                  source_lang: SL = None, split_sentences: SS = None,
                  preserve_formatting: PF = None, formality: Formality = None,
                  outline_detection: int = None, splitting_tags: List[str] = [],
                  non_splitting_tags: List[str] = [], ignore_tags: List[str] = []) -> str:
        payload = {
            'text': text,
            'tag_handling': 'xml',
            'target_lang': target_lang.value,
        }
        if source_lang:
            payload['source_lang'] = source_lang.value
        if split_sentences:
            payload['split_sentences'] = split_sentences.value
        if preserve_formatting:
            payload['preserve_formatting'] = preserve_formatting.value
        if formality:
            payload['formality'] = formality.value
        if outline_detection:
            payload['outline_detection'] = outline_detection
        if splitting_tags:
            payload['splitting_tags'] = ','.join(splitting_tags)
        if non_splitting_tags:
            payload['non_splitting_tags'] = ','.join(non_splitting_tags)
        if ignore_tags:
            payload['ignore_tags'] = ','.join(ignore_tags)
        return self._adapter.get_translated_text(payload)

    def usage(self) -> dict:
        return self._adapter.get_usage()

    def supported_languages(self) -> List[dict]:
        return self._adapter.get_supported_languages()
