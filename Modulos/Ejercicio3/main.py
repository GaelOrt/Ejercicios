from allfunctions import *

print(fecha_actual())
print(hora_actual())
fecha1 = fecha_actual()
fecha2 = date(2021, 1, 21)
print(f'Entre {fecha1} y {fecha2} hay {date_difference_days(fecha1, fecha2)} dias de diferencia')
print(get_random_password(10))
print(see_dir_content())
print(check_archive())
