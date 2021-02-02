#!/usr/bin/python3
'''API module - Task 0'''


import requests
import sys


def show_user_status():
    '''Show the currtent state of tasks for the given user id'''

    url_tasks = 'https://jsonplaceholder.typicode.com/todos?userId='
    url_users = 'https://jsonplaceholder.typicode.com/users?id='
    userId = sys.argv[1]

    # Get the name of the employee
    req_user = requests.get(url_users + userId)
    user_name = req_user.json()[0].get('name')

    # Get the tasks for the employee
    req_tasks = requests.get(url_tasks + userId)
    # Using requests.json to get a list of dicts and then get the length of it
    tasks_total = len(req_tasks.json())
    tasks_done = 0
    # Create a list to store tasks' titles
    tasks_titles = []
    for task in req_tasks.json():
        # For each task in the list if task is finished, increment tasks_done
        # and store it's name in tasks_titles
        if task.get('completed') is True:
            tasks_done += 1
            tasks_titles.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(user_name,
                                                          tasks_done,
                                                          tasks_total))
    for title in tasks_titles:
        print('\t {}'.format(title))


if __name__ == "__main__":
    show_user_status()
