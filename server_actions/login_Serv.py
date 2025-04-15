import pyodbc
import json

def handle_login(request, now, dsn, conn):
    login_name = request["data"]["login_name"]
    password = request["data"]["password"]
    print("логиним")
    try:
        conn_db = pyodbc.connect(dsn)
        cursor = conn_db.cursor()
        values = (login_name, password)

        insert_check = "SELECT [ID] FROM [Users] WHERE [login] = ? AND [Password] = ?"
        cursor.execute(insert_check, values)
        print("zapisal")
        IsLoginAndPassword = cursor.fetchall()

        insert_name = "SELECT [Name] FROM [Users] WHERE [login] = ?"
        cursor.execute(insert_name, (login_name,))
        name_from_bd = cursor.fetchone()
        name_str = name_from_bd[0]

        if IsLoginAndPassword:
            json_output_from_server = json.dumps({"name": name_str, "action": "IN"})
            conn.send(json_output_from_server.encode())

        else:
            json_output_from_server = json.dumps({"name": "Нет такого пользователя", "action": "NO"})
            conn.send(json_output_from_server.encode())

        insert_time = f"UPDATE [Users] SET [Time_log] = ? WHERE [login] = ? AND [Password] = ?"
        cursor.execute(insert_time, (now, login_name, password))
        conn_db.commit()
        print("time")
        cursor.close()
        conn_db.close()

    except Exception as e:
        print(f"Ошибка подключения: {e}")
        conn.send(f"Ошибка подключения: {e}".encode())
