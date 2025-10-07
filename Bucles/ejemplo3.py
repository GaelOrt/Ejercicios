matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for line in matriz:
    sum_ = 0
    for element in line:
        sum_ += element
    print(f'Suma fila: {sum_}')

'''
numeros = [1, 2, 3, 4, 5]
# Imprime cada número y luego crea una nueva lista con los números impares.
lista_impares_imprimiendo = [x for x in numeros if print(f"Procesando: {x}")]

print(f"\nLista final de impares: {lista_impares_imprimiendo}")
'''
