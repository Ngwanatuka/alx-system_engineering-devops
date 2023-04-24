#!/usr/bin/python3
'''script that retrieves information about an employee
using ID and exports employee task information to a JSON file'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    usr_json = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            emp_id).json()
    emp_name = usr_json.get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    emp_tasks = []

    for todo in todos:
        if todo.get("userId") == int(emp_id):
            task = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": emp_name
            }
            emp_tasks.append(task)

    filename = emp_id + ".json"

    with open(filename, 'w') as file:
        json.dump({emp_id: emp_tasks}, file)
