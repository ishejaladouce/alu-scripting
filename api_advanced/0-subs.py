#!/usr/bin/python3
"""
Module to query Reddit API for subreddit subscriber counts
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns number of subscribers for a given subreddit

    Args:
        subreddit (str): The subreddit to query

    Returns:
        int: Number of subscribers, 0 if invalid subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'alu-scripting-api-advanced'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    return 0
