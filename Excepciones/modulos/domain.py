from .logger import *


def count_words(text: str) -> int:
    write_info('Se han contado palabras del texto')
    return len(text.split())


def filter_vocals(text: str) -> str:
    replacements = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'u': '6'}
    write_info('Se han intercambiado vocales del texto')
    return ''.join([replacements.get(c, c) for c in text.lower()])


def validation_digit(text: str):
    try:
        value: int = int(text)
        write_info('Se han transformado el texto a int')
        return value
    except ValueError as e:
        write_info('Error al transformar el texto a int')
        print('No se puede convertir el texto a int:', e)
        pass
