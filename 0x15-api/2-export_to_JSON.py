#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using the JSONPlaceholder REST API and exports the data to a CSV file.
"""
import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    Url = "https://jsonplaceholder.typicode.com/users"
    url = Url + "/" + employee_id

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dict = {employee_id: []}
    for task in tasks:
        dict[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username})
    with open('{}.json'.format(employee_id), 'w') as filename:
        json.dump(dict, filename)
