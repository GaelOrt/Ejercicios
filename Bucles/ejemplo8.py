matrix: list = [[2, 5, 1], [3, 0, 4], [7, 2, 6]]
total: list = [sum(columna) for columna in zip(*matrix)]

'''
for x in range(len(matrix)):
    suma = 0
    for line in matrix:
        suma += line[x]
    total.append(suma)
'''

print(total)
