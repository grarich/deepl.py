import asyncio

import deepl

text = 'I have a pen.'

translator = deepl.Translator(deepl.AiohttpAdapter('Your API key'))


async def main():
    print(await translator.translate(text, deepl.TargetLang.Japanese))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
