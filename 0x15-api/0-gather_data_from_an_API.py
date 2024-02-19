#!/usr/bin/python3
"""
This script retrieves and displays TODO list progress for a given employee ID.
"""

from requests import get
from sys import argv


def get_todo_progress(employee_id):
    """
    Retrieve and display TODO list progress for the given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()

        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()

        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data.get('name')
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task.get('completed'))

        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in todo_data:
            if task.get('completed'):
                print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
