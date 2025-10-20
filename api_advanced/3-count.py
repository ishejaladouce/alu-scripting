#!/usr/bin/python3
"""
Module to recursively count keywords in Reddit hot posts
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively counts keywords in Reddit hot post titles

    Args:
        subreddit (str): The subreddit to query
        word_list (list): List of keywords to count
        after (str): Pagination parameter
        counts (dict): Dictionary to store word counts

    Returns:
        dict: Word counts or None if invalid subreddit
    """
    if counts is None:
        counts = {}
        for word in word_list:
            word_lower = word.lower()
            counts[word_lower] = 0

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

    for post in posts:
        title = post['data']['title'].lower()
        words_in_title = title.split()
        for word in word_list:
            word_lower = word.lower()
            counts[word_lower] += words_in_title.count(word_lower)

    after = data.get('data', {}).get('after')
    if after:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return counts
