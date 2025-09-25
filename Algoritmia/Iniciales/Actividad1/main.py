correct_password = 'admin123'
tries = 3

while tries > 0:
    password = input('Password: ')

    if password == correct_password:
        print('Correcto!')
        break
    tries -= 1
    print(f'Contraseña incorrecta, te queda(n) {tries} intento(s)')
print(f'Intentos gastados, acceso bloqueado')
