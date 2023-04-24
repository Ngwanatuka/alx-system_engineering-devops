#!/usr/bin/python3
'''script that retrieves infromation about an employee using ID and exports
employee task information to a CSV file'''

import csv
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
            task = [emp_id, emp_name, todo.get("completed"), todo.get("title")]
            emp_tasks.append(task)
    filename = emp_id + ".csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(emp_tasks)
