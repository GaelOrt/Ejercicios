exit_number = '0'

positivos = 0
negativos = 0

input_number = input('Ingrese un numero entero(0 para salir): ')

while exit_number != input_number:
    try:
        converted_input_number = int(input_number)
        if converted_input_number > 0:
            positivos += 1
            print('Se ha sumado un positivo')
        else:
            negativos += 1
            print('Se ha sumado un negativo')
    except ValueError:
        print('Debes insertar un numero entero')

    input_number = input('Ingrese un numero entero(0 para salir): ')

print('Has salido del bucle')
print(f'Numero de positivos: {positivos}')
print(f'Numero de negativos: {negativos}')
