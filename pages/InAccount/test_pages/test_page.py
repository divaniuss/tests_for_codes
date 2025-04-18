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
    user_answers = []

    def show_question(index):
        for widget in tests_in_window.winfo_children():
            widget.destroy()

        if index >= len(response):
            show_results()
            return

        question_data = response[index]
        question_text = question_data['question']
        answers = question_data['answers']

        tk.Label(tests_in_window, text=f"Вопрос {index + 1}: {question_text}", wraplength=380).pack(pady=10)

        selected_answer.set(-1)

        for i, answer in enumerate(answers):
            tk.Radiobutton(
                tests_in_window,
                text=answer["text"],
                variable=selected_answer,
                value=i
            ).pack(anchor="w")

        def next_question():
            selected_index = selected_answer.get()
            if selected_index == -1:
                messagebox.showwarning("Внимание", "Пожалуйста, выберите ответ.")
                return

            selected_text = answers[selected_index]["text"]
            is_correct = answers[selected_index]["isCorrect"]

            correct_text = ""
            for ans in answers:
                if ans["isCorrect"]:
                    correct_text = ans["text"]
                    break

            user_answers.append({
                "question": question_text,
                "selected": selected_text,
                "correct": correct_text,
                "is_correct": is_correct
            })

            current_question_index[0] += 1
            show_question(current_question_index[0])

        tk.Button(tests_in_window, text="Далее", command=next_question).pack(pady=20)

    def show_results():
        correct_count = 0
        total = len(user_answers)
        result_lines = []

        for i, answer in enumerate(user_answers, start=1):
            question = answer["question"]
            selected = answer["selected"]
            correct = answer["correct"]
            is_correct = answer["is_correct"]

            if is_correct:
                mark = "(Верно)"
                correct_count += 1
            else:
                mark = "(Неверно)"

            result_lines.append(f"{i}. {question}")
            result_lines.append(f"   Ваш ответ: {selected} {mark}")
            if not is_correct:
                result_lines.append(f"   Правильный ответ: {correct}")
            result_lines.append("")

        result_summary = f"Вы ответили правильно на {correct_count} из {total} вопросов.\n\n"
        result_text = result_summary + "\n".join(result_lines)

        messagebox.showinfo("Результаты", result_text)
        tests_in_window.destroy()

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

