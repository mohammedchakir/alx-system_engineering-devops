#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using the JSONPlaceholder REST API and exports the data to a CSV file.
"""
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dict[user_id] = []
        for task in tasks:
            dict[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username})
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dict, file)
