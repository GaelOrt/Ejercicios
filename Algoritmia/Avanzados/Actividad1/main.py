def menu_admin():
    section = ''

    while section != '1' or section != '2' or section != '3':
        print('1.Usuarios registrados')
        print('2.Añadir nuevo usuario')
        print('3.Salir')

        section = input('Elegir opción: ')

        if section == '1':
            print(f'Usuarios registrados: {users}')
            return
        if section == '2':
            new_user_name = input('Dar nombre al nuevo usuario: ')
            new_user_password = input('Dar contraseña al nuevo usuario: ')
            new_user_rol = input('Dar rol al nuevo usuario (admin/usuario): ')
            if new_user_rol != 'admin' and new_user_rol != 'usuario':
                new_user_rol = 'usuario'
            new_user = {'name': new_user_name, 'password': new_user_password, 'rol': new_user_rol}
            users.append(new_user)
            print(f'{new_user} se a añadido a la BBDD')
            return
        if section == '3':
            print('Saliendo...')
            return
        print('Opción no valida vuelve a intentarlo')


def menu_usuario(get_user):
    section = ''

    while section != '1' or section != '2' or section != '3':
        print('1.Consultar perfil')
        print('2.Cambiar contraseña')
        print('3.Salir')

        section = input('Elegir opción: ')

        if section == '1':
            print(f'Tu perfil: {get_user}')
            return
        if section == '2':
            new_password = input('Dar nueva contraseña: ')
            user['password'] = new_password
            print(f'Se ha actualizado la contraseña de tu usuario: {user}')
            return
        if section == '3':
            print('Saliendo...')
            return
        print('Opción no valida vuelve a intentarlo')


users = [{'name': 'John', 'password': '1234', 'rol': 'admin'}, {'name': 'Mike', 'password': '1234', 'rol': 'usuario'},
         {'name': 'Juan', 'password': 'adminpass', 'rol': 'usuario'},
         {'name': 'Ana', 'password': 'clave123', 'rol': 'admin'}]

tries = 3
get_out = False

while tries > 0:
    name = input('Nombre: ')
    password = input('Password: ')

    for user in users:
        if user['name'] == name and user['password'] == password:
            print('Usuario en la BBDD, registro exitoso')
            if user['rol'] == 'admin':
                menu_admin()
            else:
                menu_usuario(user)
            get_out = True
    if get_out:
        break
    tries -= 1
    print(f'El usuario no esta en la BBDD, te queda(n) {tries} intento(s)')
