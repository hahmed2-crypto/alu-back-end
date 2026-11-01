#!/usr/bin/python3
"""
Gathers data from a REST API for a given employee ID and exports
all their tasks to a file in CSV format.
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Fetches data from JSONPlaceholder API and exports it to a CSV file.
    Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    """
    url = "https://typicode.com"

    # Fetch user data
    user_res = requests.get(url + "users/{}".format(employee_id))
    user_data = user_res.json()
    username = user_data.get("username")

    # Fetch todo list items
    todos_res = requests.get(url + "todos", params={"userId": employee_id})
    todos_data = todos_res.json()

    # Write data to CSV file using standard formatting rules
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_csv(int(sys.argv[1]))

