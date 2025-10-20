#!/usr/bin/python3
"""
Module to query Reddit API for top ten hot posts
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of first 10 hot posts

    Args:
        subreddit (str): The subreddit to query
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'alu-scripting-api-advanced'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            print(post['data']['title'])
            
    except (KeyError, ValueError):
        print(None)
