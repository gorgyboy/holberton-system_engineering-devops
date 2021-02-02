#!/usr/bin/python3
'''API module - Task 2'''

import json
import requests
import sys


def export_user_status_json():
    '''
    Exports to a JSON file the tasks statuts for the given employee ID.
    The file name is "USER_ID".json.
    '''

    url_tasks = 'https://jsonplaceholder.typicode.com/todos?userId='
    url_users = 'https://jsonplaceholder.typicode.com/users?id='
    userId = sys.argv[1]
    file_name = '{}.json'.format(userId)

    # Get the username of the employee
    req_user = requests.get(url_users + userId)
    user_username = req_user.json()[0].get('username')

    # Get the tasks for the employee
    req_tasks = requests.get(url_tasks + userId)

    # Create dict and store tasks status
    tasks_status = {userId: []}
    for task in req_tasks.json():
        tasks_status.get(userId).append({"task": task.get("title"),
                                         "completed": task.get("completed"),
                                         "username": user_username})

    # Write the tasks status to file
    with open(file_name, 'w') as jsonfile:
        json.dump(tasks_status, jsonfile)


if __name__ == "__main__":
    export_user_status_json()
