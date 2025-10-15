def check_users(users_list: list) -> list:
    credentials_list = []
    for user in users_list:
        if user[1] == 'admin':
            credentials_list.append('Accepted')
            print(f'El usuario {user[0]} ha sido Aceptado')
        else:
            credentials_list.append('Denied')
            print(f'El usuario {user[0]} ha sido Denegado')
    return credentials_list
