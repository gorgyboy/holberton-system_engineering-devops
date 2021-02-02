#!/usr/bin/python3
'''API module - Task 1'''

import csv
import requests
import sys


def export_user_status_csv():
    '''
    Exports to a CSV file the tasks statuts for the given employee ID.
    The format is: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE".
    The file name is "USER_ID".csv.
    '''

    url_tasks = 'https://jsonplaceholder.typicode.com/todos?userId='
    url_users = 'https://jsonplaceholder.typicode.com/users?id='
    userId = sys.argv[1]
    file_name = '{}.csv'.format(userId)

    # Get the username of the employee
    req_user = requests.get(url_users + userId)
    user_username = req_user.json()[0].get('username')

    # Get the tasks for the employee
    req_tasks = requests.get(url_tasks + userId)

    # Open the csv file with newline='' for compatibility
    with open(file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write to file each task status
        for task in req_tasks.json():
            spamwriter.writerow([userId, user_username, task.get('completed'),
                                 task.get('title')])


if __name__ == "__main__":
    export_user_status_csv()
