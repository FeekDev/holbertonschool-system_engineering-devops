#!/usr/bin/python3
""""""
from distutils.errors import CompileError
from urllib import request
from sys import argv
from requests import get

if __name__ == '__main__':
    api_url_usr = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    response = get(api_url_usr)
    name = response.json().get('name')

    api_todos = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
    response = get(api_todos)
    tasks = response.json()
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            title = task.get('title')
            done_tasks.append(title)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(done_tasks), len(tasks)))

    for complete_task in done_tasks:
        print(f'\t {complete_task}')
