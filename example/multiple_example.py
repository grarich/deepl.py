import deepl

text = ['I have a pen.', 'I don\'t hava a pen.']

translator = deepl.Translator(deepl.RequestsAdapter('Your API key'))


def main():
    print(translator.translate_multi(text, target_lang=deepl.TargetLang.Japanese))


if __name__ == '__main__':
    main()
