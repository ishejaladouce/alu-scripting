#!/usr/bin/python3
"""Module that queries Reddit and prints the top 10 hot posts for a subreddit.

This module provides the function `top_ten(subreddit)` which prints the
titles of the first 10 hot posts for the given subreddit. If the subreddit
is invalid, a redirect occurs, or an error happens, the function prints
``None``.
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
    base_url = "https://www.reddit.com"
    endpoint = "/r/{}/hot.json".format(subreddit)
    url = base_url + endpoint
    headers = {"User-Agent": "Mozilla/5.0"}
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

    # If subreddit redirects (invalid) or response is not OK -> None
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
        if title is not None:
            print(title)
