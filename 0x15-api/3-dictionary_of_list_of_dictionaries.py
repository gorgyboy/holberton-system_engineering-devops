#!/usr/bin/python3
'''API module - Task 3'''

import json
import requests


def export_users_status_json():
    '''
    Exports to a JSON file the statuts for all employees.
    '''

    url_tasks = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    file_name = 'todo_all_employees.json'

    # Get the users and tasks data
    req_users = requests.get(url_users)
    req_tasks = requests.get(url_tasks)

    # Create dict and store tasks status for each user
    tasks_status = {}
    for user in req_users.json():
        # Foreach user get the id and username and add the key and empty list
        user_id = user.get("id")
        user_username = user.get("username")
        tasks_status[user_id] = []
        for task in req_tasks.json():
            # Foreach task we check if is user_id's task and add it to the dict
            if task.get("userId") == user_id:
                tasks_status.get(user_id).append({
                    "username": user_username,
                    "task": task.get("title"),
                    "completed": task.get("completed")})

    # Write the tasks status to file
    with open(file_name, 'w') as jsonfile:
        json.dump(tasks_status, jsonfile)


if __name__ == "__main__":
    export_users_status_json()
