:orphan:

.. _quickstart:

クイックスタート
================

ここでは、ライブラリの基本的な使用方法を説明します。
ライブラリがインストールされていることを前提としているので、
インストールを終えていない人は :ref:`installing` を参照してください。

最小限の使い方
--------------

このように書くことができます。
ファイル名は ``example_translator.py`` としましょう。
ライブラリと競合してしまうので、ファイル名は ``deepl.py`` という名前にしないでください。

- Sync 版
    .. code-block:: python3

        import deepl

        text = 'I have a pen.'
        
        translator = deepl.Translator(deepl.RequestsAdapter('Your API key'))
        
        
        def main():
            print(translator.translate(text, target_lang=deepl.TargetLang.Japanese))
        
        
        if __name__ == '__main__':
            main()
    

- Async 版
    .. code-block:: python3

        import asyncio

        import deepl
        
        text = 'I have a pen.'
        
        translator = deepl.Translator(deepl.AiohttpAdapter('Your API key'))
        
        
        async def main():
            print(await translator.translate(text, target_lang=deepl.TargetLang.Japanese))
        
        if __name__ == '__main__':
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())

最後に、APIキーを入れてアプリケーションを起動します。
APIキーの取得方法は :doc:`deepl_intro` を参照してください。

それでは実行してみましょう。

Linux, MacOS, その他のOS を使用している場合 ::

    $ python3 example_translator.py

Windowsを使用している場合は、以下のコマンドで実行してください。 ::

    $ py -3 example_translator.py

これでDeepL APIを利用した基本的なアプリケーションを作成することができました。
