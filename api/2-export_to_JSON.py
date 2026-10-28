#!/usr/bin/python3
import json
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, user_id)).json()
    todos = requests.get("{}/todos".format(url),
                         params={"userId": user_id}).json()

    tasks = [{"task": t.get("title"),
              "completed": t.get("completed"),
              "username": user.get("username")} for t in todos]

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump({str(user_id): tasks}, json_file)
