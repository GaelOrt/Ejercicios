from datetime import datetime
import string
import secrets
import os
from pathlib import Path


def fecha_hora_actual() -> tuple:
    current_time = datetime.now()
    return current_time.strftime('%d/%m/%Y'), current_time.strftime('%H:%M')


def get_random_password(number: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(number))


def see_dir_content() -> list[str]:
    contenido = os.listdir('.')
    return contenido


def check_archive(name: str = 'main.py') -> str:
    ruta_archivo = Path(name)
    if ruta_archivo.is_file():
        return f'El archivo "{ruta_archivo}" existe.'
    else:
        return f'El archivo "{ruta_archivo}" no existe.'
