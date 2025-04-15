import pyodbc


def handle_login(request, now, dsn, conn):
    print("Вход:")
    login = request["data"]["name"]
    password = request["data"]["password"]

    try:
        conn_db = pyodbc.connect(dsn)
        cursor = conn_db.cursor()
        values = (login, password)

        insert_check = "SELECT [ID] FROM [Users] WHERE [login] = ? AND [Password] = ?"
        cursor.execute(insert_check, values)
        print("zapisal")
        IsLoginAndPassword = cursor.fetchall()

        if IsLoginAndPassword:
            conn.send(f"Добро пожаловать {login}!".encode())
        else:
            conn.send(f"Нет такого пользователя".encode())

        insert_time = "UPDATE [Users] SET [Time_log] = ? WHERE [login] = ? AND [Password] = ?"
        cursor.execute(insert_time, (now, login, password))
        conn_db.commit()
        print("time")
        cursor.close()
        conn_db.close()

    except Exception as e:
        print(f"Ошибка подключения: {e}")
        conn.send(f"Ошибка подключения: {e}".encode())