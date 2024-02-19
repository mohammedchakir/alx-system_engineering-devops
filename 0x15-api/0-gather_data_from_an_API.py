#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using the JSONPlaceholder REST API.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress for the specified employee ID.
    """
    # URL for the JSONPlaceholder API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get employee information
    response = requests.get(f'{base_url}/users/{employee_id}')
    employee_data = response.json()
    employee_name = employee_data['name']

    # Get employee's TODO list
    response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos = response.json()

    # Calculate TODO list progress
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
