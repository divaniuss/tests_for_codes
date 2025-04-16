import tkinter as tk

def check_answer():
    selected = selected_option.get()
    if selected == -1:
        feedback_label.config(text="Вы не выбрали вариант.", fg="orange")
    elif selected == correct_index:
        feedback_label.config(text="Верно!", fg="green")
    else:
        correct_text = options[correct_index]
        feedback_label.config(text=f"Неверно! Правильный ответ: {correct_text}", fg="red")

root = tk.Tk()
root.title("Тест с одним выбором")

question = "Какой язык программирования используется в этом примере?"
options = ["Python", "Java", "C#", "JavaScript"]
correct_index = 0

question_label = tk.Label(root, text=question, font=("Arial", 16), wraplength=400)
question_label.pack(pady=20)

selected_option = tk.IntVar()
selected_option.set(-1)

for idx, option in enumerate(options):
    rb = tk.Radiobutton(root, text=option, variable=selected_option, value=idx, font=("Arial", 14))
    rb.pack(anchor="w")

submit_button = tk.Button(root, text="Отправить", command=check_answer)
submit_button.pack(pady=15)

feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

root.mainloop()