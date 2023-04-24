#!/usr/bin/python3
"""
Retrieves information about an employee using their ID.
"""

import requests
import sys


def main():
    """Main function"""

    # Check that the script was called with an argument
    if len(sys.argv) != 2:
        print("Usage: ./employee_todo.py EMPLOYEE_ID")
        return

    # Get the employee ID from the command line arguments
    emp_id = sys.argv[1]

    # Retrieve the user information using the provided REST API
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{emp_id}")
    user_response.raise_for_status()
    user_data = user_response.json()
    emp_name = user_data["name"]

    # Retrieve the todo list for the specified employee
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}")
    todo_response.raise_for_status()
    todo_data = todo_response.json()

    # Compute the number of completed and total tasks
    total_tasks = len(todo_data)
    completed_tasks = [t for t in todo_data if t["completed"]]
    num_completed = len(completed_tasks)

    # Extract the titles of completed tasks
    completed_titles = [t["title"] for t in completed_tasks]

    # Print the employee's progress report
    print(f"Employee {emp_name} is done with tasks({num_completed}/{total_tasks}):")
    for title in completed_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
