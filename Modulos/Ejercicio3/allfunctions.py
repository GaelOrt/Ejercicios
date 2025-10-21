from datetime import datetime, date, timedelta, time
import string
import secrets
import os
from pathlib import Path


def fecha_actual() -> date:
    current_time = datetime.now()
    return current_time.date()


def hora_actual() -> time:
    current_time = datetime.now()
    return current_time.time()


def date_difference_days(start_date: date, end_date: date) -> int:
    return (start_date - end_date).days


def get_random_password(number: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(number))


def see_dir_content() -> list[str]:
    contenido = os.listdir('.')
    return contenido


def check_archive(name: str = 'app.py') -> str:
    ruta_archivo = Path(name)
    if ruta_archivo.is_file():
        return f'El archivo "{ruta_archivo}" existe.'
    else:
        return f'El archivo "{ruta_archivo}" no existe.'
