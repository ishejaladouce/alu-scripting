#!/usr/bin/python3
"""
Module to query Reddit API for top ten hot posts
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of first 10 hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:script:v1.0 (by /u/your_username)'}
    
    try:
        response = requests.get(url, headers=headers, params={'limit': 10}, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print("None")
    except Exception:
        print("None")
