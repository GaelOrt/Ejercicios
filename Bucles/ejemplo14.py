temperatures: tuple = (12, 23, 10, 5, 34, 23, 31, 40, 15)
number_over_30: int = len([temperature for temperature in temperatures if temperature > 30])
average: float = sum(temperatures) / len(temperatures)
temperature_max: int = [index for index, temperature in enumerate(temperatures) if temperature == max(temperatures)][0]

print(f'\nCantidad de temperaturas por encima de 30: {number_over_30}', end='\n\n')
print(f'Media temperaturas: {average}', end='\n\n')
print(f'Indice temperatura maxima: {temperature_max}', end='\n\n')

for index, temperature in enumerate(temperatures):
    print(f'Dia {index + 1}: {temperature}ºC')
