alumnos = [('Ana', 8), ('Luis', 5), ('Maria', 9), ('Juan', 4)]
aptos = 0
no_aptos = 0

for alumno in alumnos:
    if alumno[1] > 5:
        aptos += 1
        print(f'El alumno {alumno[0]} es APTO')
    else:
        no_aptos += 1
        print(f'El alumno {alumno[0]} NO es APTO')

print(f'Aptos: {aptos}, No Aptos: {no_aptos}')
