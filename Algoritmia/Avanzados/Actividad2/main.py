# VALIDACIONES
import sys


def check_input(data, type_input):
    match type_input:
        case 1:
            try:
                int(data)
                return True
            except ValueError:
                return False
        case 2:
            try:
                float(data)
                return True
            except ValueError:
                return False
    return None


def validate_integer(text, min_data=0, max_data=sys.maxsize):
    integer = input(text)
    while not check_input(integer, 1) or min_data > int(integer) or max_data < int(integer):
        print(f'No es un valor valido, numero, positivo y entero, entre {min_data} y {max_data}')
        integer = input(text)
    return int(integer)


def validate_float(text, min_data=0, max_data=sys.maxsize):
    float_input = input(text)
    while not check_input(float_input, 2) or min_data > float(float_input) or max_data < float(float_input):
        print(f'No es un valor valido, positivo y float, entre {min_data} y {max_data}')
        float_input = input(text)
    return float(float_input)


def validate_string(text, len_min=1):
    string_input = input(text)
    while len_min > len(string_input.strip()):
        print(f'No es un valor valido, hace falta minimo {len_min} caracter(es)')
        string_input = input(text)
    return string_input


# Obtención del indice del producto en la lista
def get_product_index():
    product = validate_integer('Escoge un producto: ', 1, len(products))
    while int(product) > len(products):
        print('No es un producto valido, numero, positivo y entero')
        product = input('Escoge un producto: ')
    product = int(product) - 1
    return product


# Comprobar que haya productos
def check_products():
    if not products:
        print('No hay productos disponibles')
        return False
    else:
        return True


# Alerta cuando hay menos dde 5 de stock
def alert_stock():
    for product in products:
        if product['stock'] < 5:
            print(f'Cuidado {product["name"]} tiene un stock de menos de 5')


# OPCIONES DEL MENU
def list_products():
    if not check_products():
        return
    print(f'Productos listados:')
    for index, product in enumerate(products):
        print(f'{index + 1}.Producto: {product['name']}, {product['stock']} stock, {product['price']:.2f}€')


def add_product():
    new_product_name = validate_string('Dar nombre al nuevo producto: ')
    new_product_stock = validate_integer('Dar stock al nuevo producto(integer): ')
    new_product_price = validate_float('Dar precio al nuevo producto(float): ')

    new_product = {'name': new_product_name, 'stock': new_product_stock, 'price': new_product_price}
    products.append(new_product)
    print(f'{new_product} se a añadido a la BBDD')


def register_sale():
    if not check_products():
        return
    list_products()
    sale_index = get_product_index()
    if products[sale_index]['stock'] > 0:
        amount = validate_integer(
            f'Dar el numero de productos que quieres de {products[sale_index]['name']}(integer): ', 1,
            products[sale_index]['stock'])
        if products[sale_index]['stock'] < amount:
            print(
                f'La venta se cancelo, ya que la demanda de productos escogidos {amount}, supera el stock del producto {products[sale_index]['stock']}')
        else:
            products[sale_index]['stock'] -= amount
            print(f'{amount} venta(s) para el producto: {products[sale_index]}')
    else:
        print(f'No queda stock de este producto: {products[sale_index]}')


def add_stock():
    if not check_products():
        return
    list_products()
    index = get_product_index()
    stock = validate_integer('Dar el numero de stock que quieres añadir al producto(integer): ', 1)

    products[index]['stock'] += stock
    print(f'Se han añadido +{stock} de stock al producto: {products[index]}')


def exit_console():
    print('Saliendo...')


# MENU PRINCIPAL
def menu():
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
                if selected_function == exit_console:
                    break
            else:
                print("Opción no válida. Introduce un número de la lista.")

        except ValueError:
            # Maneja el caso en que la entrada no sea un número
            print("Entrada no válida. Por favor, introduce una opción.")

        print()  # Añade un espacio para mayor claridad en la consola


products = [{'name': 'Gel', 'stock': 43, 'price': 30.00}]

options = [['Listar Productos', list_products], ['Añadir Producto', add_product],
           ['Registrar Venta', register_sale], ['Reponer Stock', add_stock], ['Salir', exit_console]]

menu()



