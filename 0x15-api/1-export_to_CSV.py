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
    todos = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         emp_id + '/todos').json()

    filename = emp_id + '.csv'

    with open(filename, 'w') as csv:
        for todo in todos:
            csv.write('"{}","{}","{}","{}"\n'.format(todo.get('userId'),
                                                     emp_name,
                                                     todo.get("completed"),
                                                     todo.get("title")))
