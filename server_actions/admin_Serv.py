import pyodbc

def handle_admin(dsn, conn):
    print("Просмотр:")
    try:
        conn_db = pyodbc.connect(dsn)
        cursor = conn_db.cursor()

        cursor.execute("SELECT [ID],[Time_log],[login] FROM [Users]")
        rows = cursor.fetchall()

        result_str = ""
        for row in rows:
            result_str += f"\nID:{row[0]} Был в сети: {row[1]} Логин: {row[2]}"

        print("rez:")
        print(result_str)
        conn.send(result_str.encode())
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        conn.send(f"Ошибка подключения: {e}".encode())