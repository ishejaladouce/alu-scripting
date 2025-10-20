#!/usr/bin/python3
"""Module that queries the Reddit API and prints the top 10 hot posts
for a subreddit.

Provides the function `top_ten(subreddit)` which prints the titles of the
first 10 hot posts for the given subreddit. Prints ``None`` if the subreddit
is invalid or an error occurs.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): Name of the subreddit to query.

    Output:
        Prints one title per line for the first 10 hot posts, or prints
        ``None`` if the subreddit is invalid or an error occurs.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alx.api:0.1 (by /u/your_username)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
    except requests.exceptions.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        children = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not children:
        print(None)
        return

    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            print(title)
