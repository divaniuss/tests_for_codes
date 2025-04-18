import pyodbc
import json

def testing_serv(request, dsn, conn):
    level = request["data"]["level"]

    try:
        conn_db = pyodbc.connect(dsn)
        cursor = conn_db.cursor()

        # Получаем все вопросы нужного уровня
        select_questions = "SELECT [ID], [Text] FROM [Questions] WHERE [Level] = ? ORDER BY [ID]"
        cursor.execute(select_questions, (level,))
        questions = cursor.fetchall()

        result = []

        for question in questions:
            question_id = question.ID
            question_text = question.Text

            # Получаем все ответы на текущий вопрос
            select_answers = "SELECT [Text], [isCorrect] FROM [Answers] WHERE [QuestionID] = ? ORDER BY [ID]"
            cursor.execute(select_answers, (question_id,))
            answers = cursor.fetchall()

            answer_list = []
            for answer in answers:
                answer_list.append({
                    "text": answer.Text,
                    "isCorrect": bool(answer.isCorrect)
                })

            result.append({
                "question": question_text,
                "answers": answer_list
            })

        json_output = json.dumps(result)
        conn.send(json_output.encode())


    except Exception as e:
        print(f"Ошибка: {e}")
        conn.send(f"Ошибка подключения: {e}".encode())