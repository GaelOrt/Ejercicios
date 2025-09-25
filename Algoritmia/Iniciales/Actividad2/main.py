# OPCIONES DEL MENU
def get_balance():
    print(f'Saldo: {balance}')


def exit_console2():
    print('Saliendo...')


def retire_balance():
    global balance
    get_balance()
    retire = int(input('Cuanto dinero quieres retirar del saldo: '))

    if retire > balance:
        print('La retirada no puede ser mayor al saldo')
        return

    balance -= retire
    print(f'Se ha retirado {retire} de la cantidad del saldo')


# MENU PRINCIPAL
def simple_menu():
    while True:
        # Imprime las opciones directamente desde la lista
        for i, option in enumerate(options):
            print(f"{i + 1}. {option[0]}")

        election = input("Elegir opción: ")

        try:
            # Convertimos la elección a un número entero
            election_index = int(election) - 1

            # Verificamos si la opción está en el rango válido
            if 0 <= election_index < len(options):
                # Obtenemos la función de la lista y la ejecutamos
                selected_function = options[election_index][1]
                selected_function()

                # Si la función es para salir, rompemos el bucle
                if selected_function == exit_console2:
                    break
            else:
                print("Opción no válida. Introduce un número de la lista.")

        except ValueError:
            # Maneja el caso en que la entrada no sea un número
            print("Entrada no válida. Por favor, introduce una opción.")

        print()  # Añade un espacio para mayor claridad en la consola


balance = 30

options = [['Consultar saldo', get_balance], ['Retirar Saldo', retire_balance], ['Salir', exit_console2]]

simple_menu()
