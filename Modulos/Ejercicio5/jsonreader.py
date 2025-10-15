import json


def return_total():
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
        print("File data =", data)
        total_price = 0
        for product, values in data.items():
            total_price += values['price']
        return total_price

    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
