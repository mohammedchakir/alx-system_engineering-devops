#!/usr/bin/python3
"""
This script retrieves and displays TODO list progress for a given employee ID.
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"

    employeeId = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(employeeId))

    user = user_response.json()

    params = {"userId": employeeId}

    todos_response = requests.get(url + "todos", params=params)
   
    todos = todos_response.json()

    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks ({}/{})".format(user.get("name"),
                                                          len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
