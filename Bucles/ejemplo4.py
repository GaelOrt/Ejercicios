colors: tuple = ('rojo', 'verde', 'azul')

for index, color in enumerate(colors):
    message = f'{index + 1} {color},' if index + 1 != len(colors) else f'{index + 1} {color}'
    print(message, end=' ')
