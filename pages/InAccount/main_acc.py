import tkinter as tk
from tkinter import ttk
from pages.InAccount.test_pages.test_page import Test
from utilities.center_window import center_window


def InAccount(name, root, login_name, client):
    login_in_window = tk.Toplevel(root)
    login_in_window.title(f"Добро пожаловать {name}")
    center_window(login_in_window, 350, 300)

    level_var = tk.StringVar(value="100")

    tk.Label(login_in_window, text="Выберите http code status для начала теста:").pack(pady=(20, 5))
    level_combobox = ttk.Combobox(login_in_window, textvariable=level_var, values=["100", "200", "300", "400", "500"],state="readonly")
    level_combobox.pack()

    def Exit():
        login_in_window.destroy()

    button_width = 30
    button_pad_y = 10
    tk.Button(login_in_window, text="Начать тест", width=button_width, command= lambda : Test(root, client, int(level_var.get()))).pack(pady=button_pad_y)
    tk.Button(login_in_window, text="Выйти", width=button_width, command=Exit).pack(pady=(button_pad_y, 20))