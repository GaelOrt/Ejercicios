def ciclo(valores, max_ciclos):
    count = 0
    while count != max_ciclos:
        for value in valores:
            count += 1
            yield value


valores = ["A", "B", "C"]
for x in ciclo(valores, 7):
    print(x, end=' ')
