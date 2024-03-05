#!/usr/bin/python3
"""Query Reddit API, print titles of 10 hot posts in subreddit"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        None
    """
    if subreddit is None:
        print("None")
        return

    user_agent = {'User-Agent': 'my_bot/1.0'}
    params = {'limit': 10}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    try:
        response = get(url, headers=user_agent, params=params)
        response.raise_for_status()

        results = response.json()
        posts = results.get('data', {}).get('children', [])

        if posts:
            print(f"Top 10 hot posts in r/{subreddit}:")
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print("None")
    except Exception as e:
        print(f"An error occurred: {e}")
