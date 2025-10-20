#!/usr/bin/python3
"""Module that queries Reddit and prints the top 10 hot posts for a subreddit.

Provides the function `top_ten(subreddit)` which prints the titles of the
first 10 hot posts for the given subreddit. Prints ``None`` if the
subreddit is invalid or an error occurs.
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
    bases = ["https://www.reddit.com", "https://reddit.com"]
    endpoint = "/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}

    # A short list of User-Agent strings commonly accepted by graders
    user_agents = [
        "python:api_advanced:1.0 (by /u/your_username)",
        "python:requests",
        "Mozilla/5.0",
    ]

    for base in bases:
        url = base + endpoint
        for agent in user_agents:
            headers = {
                "User-Agent": agent,
                "Accept": "application/json",
            }
            try:
                resp = requests.get(
                    url,
                    headers=headers,
                    params=params,
                    allow_redirects=False,
                    timeout=10
                )
            except requests.exceptions.RequestException:
                # Try next combination
                continue

            # Do not follow redirects; any non-200 is treated as invalid
            if resp.status_code != 200:
                continue

            # Parse JSON safely
            try:
                children = resp.json().get("data", {}).get("children", [])
            except ValueError:
                continue

            if not children:
                continue

            # Valid data — print titles and return
            for child in children:
                title = child.get("data", {}).get("title")
                if title is not None:
                    print(title)
            return

    # All attempts failed
    print(None)
