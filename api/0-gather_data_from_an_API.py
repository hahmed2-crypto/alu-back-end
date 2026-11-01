#!/usr/bin/python3
"""
Gathers data from a REST API for a given employee ID and displays
their TODO list progress information on standard output.
"""
import requests
import sys


def fetch_employee_todo(employee_id):
    """
    Fetches employee name and todo tasks from JSONPlaceholder API
    and formats the output to match grading requirements exactly.
    """
    url = "https://typicode.com"

    # Fetch user data
    user_res = requests.get(url + "users/{}".format(employee_id))
    user_data = user_res.json()
    employee_name = user_data.get("name")

    # Fetch todo list items
    todos_res = requests.get(url + "todos", params={"userId": employee_id})
    todos_data = todos_res.json()

    # Calculate tasks tracking metrics
    completed_tasks = []
    total_tasks = 0

    for task in todos_data:
        total_tasks += 1
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    # Print summary output header line
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    # Print individual completed task titles with 1 tab and 1 space padding
    for title in completed_tasks:
        print("\t {}".format(title))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_employee_todo(int(sys.argv[1]))
