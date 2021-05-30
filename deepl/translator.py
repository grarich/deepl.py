from typing import List

from .adapter import Adapter
from .enums import Formality
from .enums import PreserveFormatting as PF
from .enums import SourceLang as SL
from .enums import SplitSentences as SS
from .enums import TargetLang as TL

__all__ = ['Translator']


class Translator:
    """
    Represents a client connection to DeepL. This class is used to interact with the DeepL API.

    Args:
        adapter (Adapter):
            An adapter for interacting with the DeepL API.
            There are two types of adapters: synchronous and asynchronous.
    """
    def __init__(self, adapter: Adapter) -> None:
        self._adapter = adapter

    def translate(self, text, *, target_lang: TL,
                  source_lang: SL = None, split_sentences: SS = None,
                  preserve_formatting: PF = None, formality: Formality = None) -> str:
        """
        A function used to translate text.

        Args:
            text (str): Text to be translated.
            target_lang (TargetLang): The language into which the text should be translated.
            source_lang (Optional[SourceLang]): Language of the text to be translated.
            split_sentences (Optional[SplitSentences]):
                Sets whether the translation engine should first split the input into sentences.
                This is enabled by default.
            preserve_formatting (Optional[PreserveFormatting]):
                Sets whether the translation engine should respect the original formatting,
                even if it would usually correct some aspects.
            formality (Optional[Formality]):
                Sets whether the translated text should lean towards formal or informal language.
                This feature currently only works for target languages
                "DE" (German)
                "FR" (French)
                "IT" (Italian)
                "ES" (Spanish)
                "NL" (Dutch)
                "PL" (Polish)
                "PT-PT"
                "PT-BR" (Portuguese)
                "RU" (Russian).
        Returns:
            str: Text translated by DeepL translation.
        """
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
        """
        A function used to translate text.

        Args:
            text (List[str]): Text list to be translated.
            target_lang (TargetLang): The language into which the text should be translated.
            source_lang (Optional[SourceLang]): Language of the text to be translated.
            split_sentences (Optional[SplitSentences]): 
                Sets whether the translation engine should first split the input into sentences.
                This is enabled by default.
            preserve_formatting (Optional[PreserveFormatting]): 
                Sets whether the translation engine should respect the original formatting,
                even if it would usually correct some aspects.
            formality (Optional[Formality]):
                Sets whether the translated text should lean towards formal or informal language.
                This feature currently only works for target languages
                "DE" (German)
                "FR" (French)
                "IT" (Italian)
                "ES" (Spanish)
                "NL" (Dutch)
                "PL" (Polish)
                "PT-PT"
                "PT-BR" (Portuguese)
                "RU" (Russian).
        Returns:
            str: Text translated by DeepL translation.
        """
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
        """Allows you to monitor how much you translate, as well as the limits set."""
        return self._adapter.get_usage()

    def supported_languages(self) -> List[dict]:
        """Sllows you to list all supported languages of the API."""
        return self._adapter.get_supported_languages()
