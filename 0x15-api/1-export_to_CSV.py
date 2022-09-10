#!/usr/bin/python3
"""
This script display the tasks completed
"""
from requests import get
import csv
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    response = get(url)
    tasks = response.json()

    with open('{}.csv'.format(argv[1]), mode='w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(argv[1], name, task.get('completed'),
                            task.get('title')))
