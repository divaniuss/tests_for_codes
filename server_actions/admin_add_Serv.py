import pyodbc
import json

def new_question_admin(request, dsn, conn):
    try:
        conn_db = pyodbc.connect(dsn)
        cursor = conn_db.cursor()
        print("добавляем:")

        level = request["data"]["level"]
        question_text = request["data"]["question"]
        answers = request["data"]["answers"]

        insert_query = "INSERT INTO [Questions] ([Level], [Text]) OUTPUT INSERTED.ID VALUES (?, ?)"
        values = (level, question_text)
        cursor.execute(insert_query, values)
        question_id = cursor.fetchone()[0]
        conn_db.commit()
        print("первый:")

        for answer in answers:
            insert_query = "INSERT INTO [Answers] ([QuestionID], [Text], [isCorrect]) VALUES (?, ?, ?)"
            values = (question_id, answer["text"], answer["isCorrect"])
            cursor.execute(insert_query, values)
        conn_db.commit()
        print("второй:")

        result_str = "YES"
        conn.send(result_str.encode())

        cursor.close()
        conn_db.close()

    except Exception as e:
        print(f"Ошибка: {e}")
        conn.send(f"Ошибка подключения: {e}".encode())
