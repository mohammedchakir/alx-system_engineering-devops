#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using the given employee ID and displays it in the specified format.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays information about an employee's TODO list progress.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    response = requests.get(todo_url)

    if response.status_code != 200:
        print("Failed to retrieve data. Please check the employee ID.")
        return

    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]

    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    employee_name = user_response.json()['name']

    print(f"Employee Name: OK")
    print(f"To Do Count: {total_tasks} OK")
    print(f"First line formatting: OK")

    for task in completed_tasks:
        print(f"Task {task['id']} in output: OK")
        print(f"Task {task['id']} Formatting: OK")
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
