#!/usr/bin/python3
'''API Adv. module - Task 2'''

import requests


def recurse(subreddit, hot_list=[], after=''):
    '''
    Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit. If no results are found for the given
    subreddit, returns None.
    '''
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0', }
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    posts = response.json().get("data").get("children")
    [hot_list.append(post.get("data").get("title")) for post in posts]
    after = response.json().get("data").get("after")
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list