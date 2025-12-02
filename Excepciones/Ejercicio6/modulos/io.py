class InputVacio(Exception):
    pass


def text_input() -> str:
    text: str = input('Introduce un texto: ')
    clean_text: str = text.lower().strip()
    try:
        if not clean_text: raise InputVacio('No se ha insertado una frase valida')
        assert len(clean_text) >= 3, "Debe haber por lo menos 3 caracteres."
    except AssertionError as e:
        print('Error de assert atrapado:', e)
    except InputVacio as e:
        print('Error de Input atrapado:', e)
    return text
