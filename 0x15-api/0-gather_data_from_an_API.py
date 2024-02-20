#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using the given employee ID and displays it in the specified format.
"""
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    Url = "https://jsonplaceholder.typicode.com/users"
    url = Url + "/" + employee_id

    response = requests.get(url)
    employee_name = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
