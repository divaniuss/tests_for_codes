import tkinter as tk
import json
from tkinter import messagebox
from utilities.center_window import center_window


def Test(root, client, level):
    tests_in_window = tk.Toplevel(root)
    tests_in_window.title("Тестирование")
    center_window(tests_in_window, 400, 400)

    json_output = json.dumps({
        "data": {"level": level},
        "action": "TESTING"
    })
    client.send(json_output.encode())
    response = json.loads(client.recv(8192).decode())

    current_question_index = [0]
    selected_answer = tk.IntVar()

    def show_question(index):
        for widget in tests_in_window.winfo_children():
            widget.destroy()

        if index >= len(response):
            messagebox.showinfo("Готово", "Вы прошли все вопросы!")
            tests_in_window.destroy()
            return

        question_data = response[index]
        question_text = question_data['question']
        answers = question_data['answers']

        tk.Label(tests_in_window, text=question_text, wraplength=380).pack(pady=10)

        selected_answer.set(-1)

        for i, answer in enumerate(answers):
            tk.Radiobutton(
                tests_in_window,
                text=answer["text"],
                variable=selected_answer,
                value=i
            ).pack(anchor="w")

        def next_question():
            current_question_index[0] += 1
            show_question(current_question_index[0])

        tk.Button(tests_in_window, text="Далее", command=next_question).pack(pady=20)

    show_question(current_question_index[0])

    # [{'question': 'Что означает код 100?', 'answers': [{'text': 'Продолжай', 'isCorrect': True},
    #                                                   {'text': 'Успешный запрос', 'isCorrect': False},
    #                                                    {'text': 'Ошибка клиента', 'isCorrect': False},
    #                                                    {'text': 'Ресурс перемещён', 'isCorrect': False}]},

    #  {'question': 'Что означает код 101?', 'answers': [{'text': 'Переключение протоколов', 'isCorrect': True},
    #                                                    {'text': 'Неавторизованный доступ', 'isCorrect': False},
    #                                                    {'text': 'Ресурс не найден', 'isCorrect': False},
    #                                                    {'text': 'Ошибка сервера', 'isCorrect': False}]},

    #  {'question': 'Что означает код 102?', 'answers': [{'text': 'Обработка продолжается', 'isCorrect': True},
    #                                                    {'text': 'Ошибка базы данных', 'isCorrect': False},
    #                                                    {'text': 'Доступ запрещён', 'isCorrect': False},
    #                                                    {'text': 'Неверный метод', 'isCorrect': False}]},

    #  {'question': 'Что означает код 103?', 'answers': [{'text': 'Ранняя подсказка', 'isCorrect': True},
    #                                                   {'text': 'Файл повреждён', 'isCorrect': False},
    #                                                   {'text': 'Редирект', 'isCorrect': False},
    #                                                   {'text': 'Файл удалён', 'isCorrect': False}]}]

