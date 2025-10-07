names: tuple = ('Ana', 'Luis', 'Maria')
ages: tuple = (23, 25, 22)

for index, tuple_ in enumerate(zip(names, ages)):
    print(f'{index + 1}. {tuple_[0]} - {tuple_[1]} años')
