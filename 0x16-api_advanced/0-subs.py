#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""
    
import requests
import json
    
    
def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    req = requests.get(url, headers={'User-agent': 'Carlos'}, 
                       allow_redirects=False)
    if req.json().get('data'):
        return req.json().get('data').get('subscribers')
    else:
        return 0
