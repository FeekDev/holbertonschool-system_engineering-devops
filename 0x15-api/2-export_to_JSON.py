#!/usr/bin/python3
"""
This script display the tasks completed
"""
from requests import get
from json import dump, dumps
from sys import argv

if __name__ == '__main__':
    usr_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(usr_id)
    response = get(url)
    username = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(usr_id)
    response = get(url)
    tasks = response.json()
    data = {usr_id: []}
    for task in tasks:
        data[usr_id].append({
                            "task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": username
                            })
    with open('{}.json'.format(usr_id), 'w') as f:
        dump(data, f)
