#!/usr/bin/python3
"""
This script retrieves and displays TODO list progress for a given employee ID.
"""
import requests
import sys


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f"{baseUrl}/{employeeId}"

    # Fetch employee name
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Employee not found")
        sys.exit(1)
    employeeName = response.json().get('name')

    # Fetch employee's tasks
    todoUrl = f"{url}/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # Count completed tasks and store them
    completed_tasks = [task for task in tasks if task.get('completed')]
    done = len(completed_tasks)

    # Print employee's progress
    print(f"Employee {employeeName} is done with tasks({done}/{len(tasks)}):")

    # Print titles of completed tasks with proper indentation
    for task in completed_tasks:
        print(f"\t{task.get('title')}")
