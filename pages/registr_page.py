import json
import hashlib
import tkinter as tk
from tkinter import messagebox

from utilities.center_window import center_window

def register(root, client):
    reg_window = tk.Toplevel(root)
    reg_window.title("Регистрация")
    center_window(reg_window, 300, 400)

    tk.Label(reg_window, text="Логин:").pack()
    login_entry = tk.Entry(reg_window)
    login_entry.pack()

    tk.Label(reg_window, text="Пароль:").pack()
    password_entry = tk.Entry(reg_window, show="*")
    password_entry.pack()

    tk.Label(reg_window, text="Повторите пароль:").pack()
    password_confirm_entry = tk.Entry(reg_window, show="*")
    password_confirm_entry.pack()

    def send_register():
        login = login_entry.get().strip()
        password = password_entry.get()
        password_confirm = password_confirm_entry.get()

        if password != password_confirm or not login or not password:
            messagebox.showerror("Ошибка", "Пароли не совпадают или пустые поля")
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        json_output = json.dumps({"data": {"name": login, "password": hashed_password}, "action": "REGISTER"})
        client.send(json_output.encode())
        response = client.recv(1024).decode()
        messagebox.showinfo("Ответ сервера", response)
        reg_window.destroy()

    tk.Button(reg_window, text="Зарегистрироваться", command=send_register).pack()