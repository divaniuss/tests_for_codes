import pyodbc


def handle_register(request, dsn, conn):
    print("Регистрация:")
    login_name = request["data"]["login_name"]
    name = request["data"]["name"]
    password = request["data"]["password"]
    try:
        conn_db = pyodbc.connect(dsn)
        cursor = conn_db.cursor()

        print("pihaem")
        insert_query = "INSERT INTO [Users] ([Name], [login], [Password]) VALUES (?, ?, ?)"
        values = (name, login_name, password)
        cursor.execute(insert_query, values)
        cursor.commit()
        conn_db.commit()
        print("Записано")
        result_str = "Данные успешно сохранены"
        conn.send(result_str.encode())

        cursor.close()
        conn_db.close()
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        if "23000" in str(e):
            conn.send("Этот логин уже существует".encode())
        else:
            result_str = f"Ошибка подключения: {e}"
            conn.send(result_str.encode())