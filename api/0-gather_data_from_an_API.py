#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, user_id)).json()
    todos = requests.get("{}/todos".format(url),
                         params={"userId": user_id}).json()

    done = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
