#!/usr/bin/python3
"""
This script display the tasks completed
"""
from requests import get
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    response = get(url)
    tasks = response.json()
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            title = task.get('title')
            done_tasks.append(title)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(done_tasks), len(tasks)))

    for complete_task in done_tasks:
        print("\t {}". format(complete_task))
