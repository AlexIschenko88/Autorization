import sqlite3


class DataBaseWord:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def create_db():
        password_data = sqlite3.connect('my_database.db')
        cursor = password_data.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        )
        ''')
        password_data.commit()
        password_data.close()

    def check_account(self):
        password_data = sqlite3.connect('my_database.db')
        cursor = password_data.cursor()
        cursor.execute(f'''
        SELECT * FROM Users WHERE username = '{self.login}'
        AND password = {self.password}
        ''')
        result = cursor.fetchall()
        password_data.close()
        return result

    def create_account(self):
        if not self.check_account():
            password_data = sqlite3.connect('my_database.db')
            cursor = password_data.cursor()
            cursor.execute(f'''
            INSERT INTO Users (username, password) VALUES 
            ('{self.login}', {self.password})
            ''')
            password_data.commit()
            password_data.close()
            return f'Логин и пароль добавлены в базу данных'
        else:
            return f'Такой логин и пароль уже существуют'



