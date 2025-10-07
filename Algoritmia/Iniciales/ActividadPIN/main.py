# Input con validación para integers
"""
def validate_int(data: str) -> int:
    try:
        return int(input(data))
    except ValueError:
        print('El valor ingresado no es valido, debe ser un numero')
        return -1
"""

def validate_int(data: str) -> int | None:
    str_input: str = input(data)
    if str_input.isdigit():
        return int(str_input)
    print('El valor ingresado no es valido, debe ser un numero')
    return None


# Variables
correct_pin: int = 1234
tries: int = 3

# Bucle de intentos de acceso
while tries > 0:
    tries -= 1

    pin: int = validate_int('Ingrese un número: ')

    if pin == correct_pin:
        print('PIN Correcto')
        break

    print(f'Pin incorrecto, te quedan {tries} intentos\n')

else:
    print('Te quedaste sin intentos')
