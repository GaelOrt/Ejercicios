tuple_: tuple = (10, 12, 7, 14, 9)
total: list = []
average: float = sum(tuple_) / len(tuple_)

for number in tuple_:
    if number > average:
        total.append(number)

print(f'La media es {average}')
print(f'{len(total)} elementos superan la media')
