import json
import hashlib
import tkinter as tk
from tkinter import messagebox

from utilities.center_window import center_window

def login(root, client):
    login_window = tk.Toplevel(root)
    login_window.title("Логин")
    center_window(login_window, 300, 150)

    tk.Label(login_window, text="Логин:").pack()
    login_entry = tk.Entry(login_window)
    login_entry.pack()

    tk.Label(login_window, text="Пароль:").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    def send_login():
        login = login_entry.get().strip()
        password = password_entry.get()

        if not login or not password:
            messagebox.showerror("Ошибка", "Поля не должны быть пустыми")
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        json_output = json.dumps({"data": {"name": login,
                                           "password": hashed_password},
                                  "action": "LOGIN"})
        client.send(json_output.encode())
        response = client.recv(1024).decode()
        messagebox.showinfo("Ответ сервера", response)
        login_window.destroy()

    tk.Button(login_window, text="Войти", command=send_login).pack()