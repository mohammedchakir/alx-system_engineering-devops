#!/usr/bin/python3
"""Query Reddit API, parse hot articles, print sorted count of keywords."""

import json
from requests import get


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count occurrences.
        after (str): Parameter used for pagination to get next set of results.
        word_counts (dict): Dictionary to store the counts of keywords.
    Returns:
        None
    """
    if after is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'api_advanced-project'}
    params = {'after': after}

    response = get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            title = topic['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        after = data['data']['after']
        if after is None:
            sorted_counts = sorted(counts.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
        else:
            count_words(subreddit, word_list, after, counts)
