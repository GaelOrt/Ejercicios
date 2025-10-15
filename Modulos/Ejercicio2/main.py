from entrada import *
from salida import *
from texto_utils import contar_palabras

# 1.Número par o impar: Escribe un programa que pida un número entero y muestre si es par o impar
number: int = validate_int('Introduce un numero: ')
print(show_result_pair(number))
print(f'{contar_palabras(show_result_pair(number))} palabras')
