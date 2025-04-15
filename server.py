import socket
import pyodbc
import json
from datetime import datetime

from server_actions.admin_Serv import handle_admin
from server_actions.login_Serv import handle_login
from server_actions.registr_Serv import handle_register

server_base = r'localhost\SQLEXPRESS'
database = 'db_logins'
dsn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_base};DATABASE={database};Trusted_Connection=yes'

IP = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)
print("Сервер запущен, ожидание подключения...")

conn, addr = server.accept()
print(f"Подключение от: {addr}")


def handle_bye():
    print("Закрытие..")
    conn.send("Всего доброго".encode())


while True:
    request = json.loads(conn.recv(1024).decode())
    now = str(datetime.now())
    action = request["action"]
    print(f"Принято: \n{request}")

    if action == "ADMIN":
        handle_admin(dsn, conn)
    elif action == "LOGIN":
        handle_login(request, now, dsn, conn)
    elif action == "REGISTER":
        handle_register(request, dsn, conn)
    elif action == "BYE":
        handle_bye()
        break
    else:
        print(f"Неизвестное действие: {action}")
        conn.send(f"Неизвестная команда: {action}".encode())

conn.close()
server.close()