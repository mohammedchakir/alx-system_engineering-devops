#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: The number of subscribers for the subreddit.
        Returns 0 if the subreddit is invalid.
    """
    try:
        user_agent = {'User-Agent': 'MyBot/1.0'}
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = get(url, headers=user_agent)

        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            print(f"Error: Unable to access subreddit '{subreddit}'")
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
