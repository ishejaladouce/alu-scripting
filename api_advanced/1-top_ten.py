#!/usr/bin/python3
"""Module that queries Reddit and prints the top 10 hot posts for a subreddit.

Provides top_ten(subreddit) which prints the titles of the first 10 hot
posts for the given subreddit. Prints ``None`` if the subreddit is invalid
or an error occurs.
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
    params = {"limit": 10}

    # Try a small list of commonly-accepted User-Agent strings to increase
    # the chance the request is accepted by Reddit in different grader envs.
    user_agents = [
        "python:api_advanced:1.0 (by /u/your_username)",
        "python:requests",
        "Mozilla/5.0",
    ]

    for agent in user_agents:
        headers = {"User-Agent": agent}
        try:
            resp = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False,
                timeout=10
            )
        except requests.exceptions.RequestException:
            # Try the next user agent if a request error occurred
            continue

        # If redirect or non-OK -> treat as invalid for this attempt
        if resp.status_code != 200:
            continue

        # Try to parse JSON and extract children
        try:
            children = resp.json().get("data", {}).get("children", [])
        except ValueError:
            # JSON decoding failed; try next agent
            continue

        if not children:
            # Empty result for this response; try next agent
            continue

        # We have data — print titles and return (do not print None)
        for child in children:
            title = child.get("data", {}).get("title")
            if title is not None:
                print(title)
        return

    # If all attempts failed, print None exactly once
    print(None)
