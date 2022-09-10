#!/usr/bin/python3
"""
This script display the tasks completed
"""
from requests import get
from json import dump

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    data = {}
    for usr in users:
        usr_id = usr.get('id')
        username = usr.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(usr_id)
        url = url + '/todos'
        response = get(url)
        tasks = response.json()
        data[usr_id] = []
        for task in tasks:
            data[usr_id].append({
                            "task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": username
                            })
    with open('todo_all_employees.json.json', 'w') as f:
        dump(data, f)
