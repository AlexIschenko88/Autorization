from main import DataBaseWord


def authorization():
    """
    Главный цикл программы, который отсылает к другим функциям

    Данная функция запрашивает команды у пользователя, при вводе которых,
    пользователь может авторизоваться(1), зарегистрироваться(2),
    либо выйти из программы(3)
    Return: None
    """

    while True:
        print('''Добро пожаловать! Выберите пункт меню:
        1. Вход
        2. Регистрация
        3. Выход''')

        user_input = input()

        if user_input == '1':
            print('Введите логин и пароль')
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            name = DataBaseWord(login, password)
            if name.check_account():
                print(f'Вы вошли в свой аккаунт')
            else:
                print(f'Ошибка входа. Повторите попытку!')

        elif user_input == '2':
            print('(логин должен содержать не менее'
                  ' 3 и не более 20 символов)')
            login = input('Введите логин: ')
            print('(пароль должен содержать не менее'
                  ' 4 и не более 32 символов)')
            password = input('Введите пароль: ')
            name = DataBaseWord(login, password)
            print(name.create_account())

        elif user_input == '3':
            print('Завершение работы')
            break


if __name__ == '__main__':
    authorization()
