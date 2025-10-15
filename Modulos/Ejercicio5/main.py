from logger import *
from usuarios import users_list
from autenticacion import check_users
from jsonreader import return_total


def multiplicar(num1, num2):
    """Esta función toma dos números y devuelve su producto."""
    registrar_evento('Devueltos los números multiplicados')
    return float(num1) * float(num2)


def main():
    """Coge dos números, los multiplica y muestra el resultado."""
    registrar_evento('Ejecutada función principal del script')
    num1 = 2
    num2 = 3

    resultado = multiplicar(num1, num2)

    registrar_evento('Terminado el script')
    print(f"El resultado de la multiplicación es: {resultado}")


# Asegura que la función main se ejecute solo cuando el script se ejecuta directamente
if __name__ == "__main__":
    main()

    check_users(users_list())
    print(return_total())
