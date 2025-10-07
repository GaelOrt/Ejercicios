search_number = 5

for number in range(10):
    print(number)
    if number == search_number:
        print('¡Encontrado!')
        break
else:
    print(f'No hay numero {search_number}')
