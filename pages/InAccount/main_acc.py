import tkinter as tk

from utilities.center_window import center_window


def InAccount(name, root, login_name, client):
    login_in_window = tk.Toplevel(root)
    login_in_window.title(f"Добро пожаловать {name}")
    center_window(login_in_window, 350, 300)

    def Exit():
        login_in_window.destroy()

    button_width = 30
    button_pad_y = 10
    # tk.Button(login_in_window, text="Добавить новую еду", width=button_width, command= lambda : AddFood(root, client, login_name)).pack(pady=button_pad_y)
    # tk.Button(login_in_window, text="Посмотреть, что вы сегодня съели", width=button_width, command= lambda : AllFood(root, client, login_name)).pack(pady=button_pad_y)
    tk.Button(login_in_window, text="Выйти", width=button_width, command=Exit).pack(pady=(button_pad_y, 20))