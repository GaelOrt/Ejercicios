import modulos.io as io
import modulos.domain as domain


def app():
    text: str = io.text_input()
    print(domain.count_words(text))
    print(domain.filter_vocals(text))
    print(domain.validation_digit(text))


app()
