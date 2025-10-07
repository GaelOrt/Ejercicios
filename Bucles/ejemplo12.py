grupos = [[('Ana', 8), ('Luis', 5)], [('Maria', 9), ('Juan', 4)]]
resultados = [{'Aptos': 0, 'NoAptos': 0} for _ in range(len(grupos))]

for index, grupo in enumerate(grupos):
    for alumno in grupo:
        if alumno[1] > 5:
            resultados[index]['Aptos'] += 1
            print(f'El alumno {alumno[0]} es APTO')
        else:
            resultados[index]['NoAptos'] += 1
            print(f'El alumno {alumno[0]} NO es APTO')
    print(
        f'En el Grupo {index + 1}, los Aptos: {resultados[index]['Aptos']}, y los No Aptos: {resultados[index]['NoAptos']}')

total = [sum(columna.values()) for columna in resultados]
print(f'En Total, Aptos: {total[0]}, No Aptos: {total[1]}')
