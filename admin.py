import json
import socket
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

from utilities.center_window import center_window

IP = '127.0.0.1'
PORT = 4000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.settimeout(3)

root = tk.Tk()
root.title("Admin-panel")
center_window(root, 500, 550)


text_response = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25)
text_response.pack(pady=10, padx=10)
text_response.config(state=tk.DISABLED)

import tkinter as tk
from tkinter import messagebox
from utilities.center_window import center_window
import json


def new():
    add_window_admin = tk.Toplevel(root)
    add_window_admin.title("Добавить вопрос")
    center_window(add_window_admin, 400, 450)

    tk.Label(add_window_admin, text="Введите код теста (100 / 200 / 300 / 400 / 500):").pack()
    test_entry = tk.Entry(add_window_admin)
    test_entry.pack()

    tk.Label(add_window_admin, text="Введите вопрос:").pack()
    question_entry = tk.Entry(add_window_admin)
    question_entry.pack()

    answer_entries = []
    right_answer_var = tk.IntVar(value=-1)

    for i in range(4):
        frame = tk.Frame(add_window_admin)
        frame.pack(anchor="w", pady=2)

        tk.Label(frame, text=f"Ответ {i + 1}:").pack(side="left")
        entry = tk.Entry(frame, width=30)
        entry.pack(side="left", padx=5)
        answer_entries.append(entry)

        tk.Radiobutton(frame, text="Верный", variable=right_answer_var, value=i).pack(side="left")

    def send_new():
        level_of_test = test_entry.get().strip()
        question = question_entry.get().strip()

        # Получаем текст каждого ответа по отдельности
        answer1 = answer_entries[0].get().strip()
        answer2 = answer_entries[1].get().strip()
        answer3 = answer_entries[2].get().strip()
        answer4 = answer_entries[3].get().strip()

        # Проверка уровня
        if level_of_test not in ["100", "200", "300", "400", "500"]:
            messagebox.showerror("Ошибка", "Код теста должен быть одним из: 100, 200, 300, 400, 500.")
            return

        # Проверка заполнения всех полей
        if question == "" or answer1 == "" or answer2 == "" or answer3 == "" or answer4 == "":
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
            return

        if right_answer_var.get() == -1:
            messagebox.showerror("Ошибка", "Выберите правильный ответ.")
            return

        answers = []
        for i, text in enumerate([answer1, answer2, answer3, answer4]):
            answer_dict = {
                "text": text,
                "isCorrect": (i == right_answer_var.get())
            }
            answers.append(answer_dict)

        data = {
            "action": "ADMINNEW",
            "data": {
                "level": int(level_of_test),
                "question": question,
                "answers": answers
            }
        }
        json_output = json.dumps(data)
        print(json_output)
        try:
            client.send(json_output.encode())
            messagebox.showinfo("Успех", "Вопрос успешно добавлен.")
            add_window_admin.destroy()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось отправить данные: {e}")

    tk.Button(add_window_admin, text="Отправить", command=send_new).pack(pady=15)

def admin():
    json_output = json.dumps({"data": '', "action": "ADMIN"})
    client.send(json_output.encode())
    response = client.recv(8192).decode()

    text_response.config(state=tk.NORMAL)
    text_response.delete(1.0, tk.END)
    text_response.insert(tk.END, response)
    text_response.config(state=tk.DISABLED)

def exit_app():
    json_output = json.dumps({"data": "", "action": "BYE"})
    client.send(json_output.encode())
    client.close()
    root.destroy()

tk.Button(root, text="Добавть вопрос", command = new).pack(pady=5)
tk.Button(root, text="Смотреть логи", command = admin).pack(pady=5)
tk.Button(root, text="Выход", command=exit_app).pack(pady=5)

root.mainloop()
