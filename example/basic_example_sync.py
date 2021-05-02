import deepl

text = 'I have a pen.'

translator = deepl.Translator(deepl.RequestsAdapter('Your API key'))


def main():
    print(translator.translate(text, deepl.TargetLang.Japanese))


if __name__ == '__main__':
    main()
