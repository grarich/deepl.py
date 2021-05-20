"""
DeepL API Wrapper
~~~~~~~~~~~~~~~~~~~
A basic wrapper for the DeepL API.
:copyright: (c) 2021-present grarich
:license: MIT, see LICENSE for more details.
"""

__title__ = 'deepl'
__author__ = 'grarich'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present grarich'
__version__ = '1.0.1'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .adapter import Adapter, AiohttpAdapter, RequestsAdapter
from .enums import Formality, PreserveFormatting, SourceLang, SplitSentences, TargetLang
from .translator import Translator

__all__ = [
    'Adapter',
    'RequestsAdapter',
    'AiohttpAdapter',
    'SourceLang',
    'TargetLang',
    'SplitSentences',
    'PreserveFormatting',
    'Formality',
    'Translator'
]
