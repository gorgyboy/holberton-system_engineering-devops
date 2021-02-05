#!/usr/bin/python3
'''API Adv. module - Task 0'''

import requests


def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API and returns the number of total subscribers
    for a given subreddit. If an invalid subreddit is given, returns 0.
    '''

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    else:
        return response.json().get('data').get('subscribers')
