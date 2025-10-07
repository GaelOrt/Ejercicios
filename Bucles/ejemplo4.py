colors: tuple = ('rojo', 'verde', 'azul')

for index, color in enumerate(colors):
    print_ = f'{index + 1} {color}'
    message = print_ + ',' if index + 1 != len(colors) else print_
    print(message, end=' ', sep=',')
