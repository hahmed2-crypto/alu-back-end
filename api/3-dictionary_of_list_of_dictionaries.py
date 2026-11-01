#!/usr/bin/python3
"""
Gathers all tasks from all employees from a REST API and exports
the entire database dump into a single file in JSON format.
"""
import json
import requests


def export_all_to_json():
    """
    Fetches all users and all todo data and structures it into JSON format.
    File name must be: todo_all_employees.json
    """
    url = "https://typicode.com"

    # Fetch all users to build an ID-to-username lookup dictionary
    users_res = requests.get(url + "users")
    users_data = users_res.json()

    user_dict = {}
    for user in users_data:
        user_dict[user.get("id")] = user.get("username")

    # Fetch all todo items
    todos_res = requests.get(url + "todos")
    todos_data = todos_res.json()

    # Build the collective JSON structure mapping all workers
    all_tasks_data = {}
    for user_id in user_dict.keys():
        all_tasks_data[str(user_id)] = []

    for task in todos_data:
        u_id = task.get("userId")
        if str(u_id) in all_tasks_data:
            all_tasks_data[str(u_id)].append({
                "username": user_dict.get(u_id),
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    # Write final mapped tracking data to disk
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as json_file:
        json.dump(all_tasks_data, json_file)


if __name__ == "__main__":
    export_all_to_json()
