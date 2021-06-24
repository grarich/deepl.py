from typing import Optional
from pydantic import BaseModel
from .enums import SourceLang, TargetLang, SplitSentences, PreserveFormatting, Formality, FileStatus


class TranslatedText(BaseModel):
    source_language: SourceLang
    target_language: TargetLang
    text: str
    split_sentences: Optional[SplitSentences] = None
    preserve_formatting: Optional[PreserveFormatting] = None
    formality: Optional[Formality] = None


class TranslatedXML(BaseModel):
    source_language: SourceLang
    target_language: TargetLang
    text: str
    split_sentences: Optional[SplitSentences] = None
    preserve_formatting: Optional[PreserveFormatting] = None
    formality: Optional[Formality] = None


class TranslatedFile(BaseModel):
    source_language: SourceLang
    target_language: TargetLang
    document_id: str
    document_key: str
    data: Optional[str] = None
    status: FileStatus
    seconds_remaining: Optional[int] = None
    billed_characters: Optional[int]
    split_sentences: Optional[SplitSentences] = None
    preserve_formatting: Optional[PreserveFormatting] = None
    formality: Optional[Formality] = None



class Usage(BaseModel):
    character_count: int
    character_limit: int
