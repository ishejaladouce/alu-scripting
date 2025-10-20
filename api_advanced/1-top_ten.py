#!/usr/bin/python3
"""
Module to query Reddit API for top ten hot posts
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'alu-scripting-api-advanced'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, 
                          allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
