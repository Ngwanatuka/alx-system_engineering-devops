#!/usr/bin/python3

'''script that retrieves information about all
employees and their tasks, and exports the data in JSON format'''

import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    employee_tasks = {}

    for user in users:
        user_tasks = []
        for todo in todos:
            if todo.get("userId") == user.get("id"):
                task = {"username": user.get("username"),
                        "task": todo.get("title"),
                        "completed": todo.get("completed")}
                user_tasks.append(task)
        employee_tasks[user.get("id")] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(employee_tasks, file)
