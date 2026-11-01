#!/usr/bin/python3
"""
Gathers data from a REST API for a given employee ID and exports
the tasks info into a file in JSON format.
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """
    Fetches data from JSONPlaceholder API and exports it to a JSON file.
    Format: { "USER_ID": [{"task": "...", "completed": ..., "username": "..."}, ...]}
    """
    url = "https://typicode.com"

    # Fetch user data
    user_res = requests.get(url + "users/{}".format(employee_id))
    user_data = user_res.json()
    username = user_data.get("username")

    # Fetch todo list items
    todos_res = requests.get(url + "todos", params={"userId": employee_id})
    todos_data = todos_res.json()

    # Construct the JSON data dictionary structure
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_data = {str(employee_id): tasks_list}

    # Write dictionary to JSON file
    filename = "{}.json".format(employee_id)
    with open(filename, mode='w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_json(int(sys.argv[1]))

