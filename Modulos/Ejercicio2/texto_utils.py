def contar_palabras(text: str) -> int:
    return len(text.split())


def invertir_texto(text: str) -> str:
    return text[::-1]


def detectar_palindromo(text: str) -> bool:
    return text == text[::-1]
