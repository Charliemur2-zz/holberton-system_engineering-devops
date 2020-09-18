#!/usr/bin/python3

"""
Write a recursive function that queries the Reddit
API and returns a list containing the titles of all
hot articles for a given subreddit. If no results are
found for the given subreddit, the function should return None.
"""


import requests


def recurse(subreddit, hot_list=[]):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(url, headers={'User-agent': 'Carlos'},
                       allow_redirects=False)
    if req.json().get('data'):
        for posts in req.json().get('data').get('children'):
            hot_list.append(posts.get('data').get('title'))
        return hot_list
    else:
        return ('None')
