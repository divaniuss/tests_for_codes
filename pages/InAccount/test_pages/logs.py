import json

def send_logs(login_name, level, correct_count, total, client):


    answers = f"{correct_count}/{total}"

    json_output = json.dumps({
        "data": {"level": level,
                 "login_name" : login_name,
                 "answers" : answers},
        "action": "LOGS"
    })
    client.send(json_output.encode())