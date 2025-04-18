import pyodbc

def logs_serv(request, dsn, conn, now):

    login_name = request["data"]["login_name"]
    test = request["data"]["level"]
    answers = request["data"]["answers"]
    try:
        conn_db = pyodbc.connect(dsn)
        cursor = conn_db.cursor()

        print("logiruem")
        insert_query = "INSERT INTO [Logs] ([User], [Test], [Answers], [Time_log]) VALUES (?, ?, ?, ?)"
        values = (login_name, test, answers, now)
        cursor.execute(insert_query, values)
        cursor.commit()
        conn_db.commit()
        print("Записано")
        result_str = "Данные успешно сохранены"
        conn.send(result_str.encode())

        cursor.close()
        conn_db.close()
    except Exception as e:
        print(f"Ошибка: {e}")
        conn.send(f"Ошибка подключения: {e}".encode())
