#!/usr/bin/python3
"""
Module to recursively query Reddit API for all hot posts
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries Reddit API and returns list of all hot post titles

    Args:
        subreddit (str): The subreddit to query
        hot_list (list): List to accumulate post titles
        after (str): Pagination parameter for next page

    Returns:
        list: List of all hot post titles, None if invalid subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'alu-scripting-api-advanced'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
        return hot_list if hot_list else None

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data.get('data', {}).get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
