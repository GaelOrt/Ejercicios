# 5.1 Error típico: dividir sin validar
def dividir(a, b):
    return a / b


def flujo():
    datos = [(10, 2), (5, 0), (3, 1)]
    resultados = []
    for a, b in datos:
        try:
            r = dividir(a, b)  # breakpoint aquí: ¿qué pasa con (5, 0)?
        except ZeroDivisionError:
            print('No se puede dividir por 0')
            continue
        resultados.append(r)
    return resultados


print(flujo())  # provoca ZeroDivisionError en la segunda tupla
