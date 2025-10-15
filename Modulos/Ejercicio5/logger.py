def registrar_evento(mensaje: str) -> None:
    fichero = open("logs.txt", 'a', encoding='utf-8')
    fichero.write(mensaje + '\n')
    fichero.close()
