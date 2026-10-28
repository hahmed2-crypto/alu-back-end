#!/usr/bin/python3
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, user_id)).json()
    todos = requests.get("{}/todos".format(url),
                         params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user.get("username"),
                             task.get("completed"), task.get("title")])
