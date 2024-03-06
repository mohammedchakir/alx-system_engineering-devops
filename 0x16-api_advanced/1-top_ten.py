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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/0.1'}
    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
