def validate_int(data: str) -> int:
    try:
        return int(input(data))
    except ValueError:
        print('El valor ingresado no es valido, debe ser un numero')
        return -1


correct_pin: int = 1234
tries: int = 3

while True:
    pin: int = validate_int('Ingrese un número: ')

    tries -= 1
    if tries <= 0:
        print('Te quedaste sin intentos')
        break

    if pin == correct_pin:
        print('PIN Correcto')
        break

    print(f'Pin incorrecto, te quedan {tries} intentos')
    print(' ')
