#!/usr/bin/python3
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(url)).json()
    todos = requests.get("{}/todos".format(url)).json()

    data = {}
    for user in users:
        user_id = user.get("id")
        data[str(user_id)] = [{"username": user.get("username"),
                               "task": t.get("title"),
                               "completed": t.get("completed")}
                              for t in todos if t.get("userId") == user_id]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)
