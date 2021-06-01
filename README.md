# deepl.py

A Python wrapper for the DeepL API
  
[![GitHub license](https://img.shields.io/github/license/grarich123/deepl.py)](https://github.com/grarich123/deepl.py/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/grarich123/deepl.py)](https://github.com/grarich123/deepl.py/issues)
[![GitHub forks](https://img.shields.io/github/forks/grarich123/deepl.py)](https://github.com/grarich123/deepl.py/network)
[![GitHub stars](https://img.shields.io/github/stars/grarich123/deepl.py)](https://github.com/grarich123/deepl.py/stargazers)
[![check](https://github.com/grarich123/deepl.py/actions/workflows/check.yml/badge.svg)](https://github.com/grarich123/deepl.py/actions/workflows/check.yml)
[![PyPI version](https://badge.fury.io/py/deepl.py.svg)](https://badge.fury.io/py/deepl.py)
[![Python Versions](https://img.shields.io/pypi/pyversions/deepl.py.svg)](https://pypi.org/project/deepl.py/)
[![Downloads](https://static.pepy.tech/personalized-badge/deepl-py?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads)](https://pepy.tech/project/deepl-py)

  
# installing  
Install and update using pip:

`pip install deepl.py`  

A simple example.  
  
```python
# Sync Sample

import deepl

text = 'I have a pen.'

translator = deepl.Translator(deepl.RequestsAdapter('Your API key'))


def main():
    print(translator.translate(text, target_lang=deepl.TargetLang.Japanese))


if __name__ == '__main__':
    main()
```
  
```python
#Async Sample

import asyncio

import deepl

text = 'I have a pen.'

translator = deepl.Translator(deepl.AiohttpAdapter('Your API key'))


async def main():
    print(await translator.translate(text, target_lang=deepl.TargetLang.Japanese))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
  
# Thank you to everyone who Helped me (#^^#)
