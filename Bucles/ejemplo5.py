names: tuple = ('Ana', 'Luis', 'Maria')
ages: tuple = (23, 25, 22)

for name, age in zip(names, ages):
    print(f'{name} tiene {age} años')
