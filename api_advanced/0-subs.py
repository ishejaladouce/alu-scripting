#!/usr/bin/python3
"""
Function to query Reddit API and get number of subscribers for a subreddit
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
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'alu-scripting-api-advanced'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If redirect or not found, return 0
        if response.status_code != 200:
            return 0
            
        data = response.json()
        return data['data']['subscribers']
        
    except requests.RequestException:
        return 0
    except (KeyError, ValueError):
        return 0
