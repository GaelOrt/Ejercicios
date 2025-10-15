def validate_int(data: str) -> int | None:
    try:
        return int(input(data))
    except ValueError:
        print('El valor ingresado no es valido, debe ser un numero entero')
        return None
