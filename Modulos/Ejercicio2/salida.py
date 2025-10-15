from procesamiento import *


def show_result_pair(number: int):
    if check_pair(number):
        return f'El numero {number} es un numero par'
    else:
        return f'El numero {number} No es un numero par'
