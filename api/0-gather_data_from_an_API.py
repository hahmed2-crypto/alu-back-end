#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv)< 2:
        sys.exit(1)


    user_id= sys.argv[1]
    url_user= "https://typicode.com{}".format(user_id)
    url_todo= "https://typicode.com{}".format(user_id)
    user_res= requests.get(url_user).json()
    todos_res= requests.get(url_todo).json()

    employee_name= user_res.get("name")

    completed_tasks= []
    total_tasks= 0

    for task in todos_res:
        total_tasks= +1
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))

    for title in completed_tasks:
        print("\t {}".format(title))