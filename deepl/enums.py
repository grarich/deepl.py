from enum import Enum

__all__ = [
    'SourceLang',
    'TargetLang',
    'SplitSentences',
    'PreserveFormatting',
    'Formality'
]


class SourceLang(Enum):
    Bulgarian = 'BG'
    Czech = 'CS'
    Danish = 'DA'
    German = 'DE'
    Greek = 'EL'
    English = 'EN'
    Spanish = 'ES'
    Estonian = 'ET'
    Finnish = 'FI'
    French = 'FR'
    Hungarian = "HU"
    Italian = "IT"
    Japanese = "JA"
    Lithuanian = "LT"
    Latvian = "LV"
    Dutch = "NL"
    Polish = "PL"
    Portuguese = "PT"
    Romanian = "RO"
    Russian = "RU"
    Slovak = "SK"
    Slovenian = "SL"
    Swedish = "SV"
    Chinese = "ZH"


class TargetLang(Enum):
    Bulgarian = 'BG'
    Czech = 'CS'
    Danish = 'DA'
    German = 'DE'
    Greek = 'EL'
    English = 'EN'
    English_GB = 'EN-GB'
    English_US = 'EN-US'
    Spanish = 'ES'
    Estonian = 'ET'
    Finnish = 'FI'
    French = 'FR'
    Hungarian = 'HU'
    Italian = 'IT'
    Japanese = 'JA'
    Lithuanian = 'LT'
    Latvian = 'LV'
    Dutch = 'NL'
    Polish = 'PL'
    Portuguese = 'PT-PT'
    Portuguese_BR = 'PT-BR'
    Portuguese_PT = 'PT'
    Romanian = 'RO'
    Russian = 'RU'
    Slovak = 'SK'
    Slovenian = 'SL'
    Swedish = 'SV'
    Chinese = 'ZH'


class SplitSentences(Enum):
    enabled = 0
    disabled = 1


class PreserveFormatting(Enum):
    respect = 1
    ignore = 2


class Formality(Enum):
    default = 'default'
    more = 'more'
    less = 'less'
