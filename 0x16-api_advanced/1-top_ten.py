#!/usr/bin/python3
'''API Adv. module - Task 1'''

import requests


def top_ten(subreddit):
    '''
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    '''

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0', }
    top = {'limit': 10}
    response = requests.get(url, headers=headers, params=top,
                            allow_redirects=False)
    if response.status_code != 200:
        return print('None')
    results = response.json().get('data')
    for top in results.get("children"):
        print(top.get("data").get("title"))
