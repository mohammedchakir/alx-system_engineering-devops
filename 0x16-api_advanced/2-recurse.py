#!/usr/bin/python3
"""Recursive function queries the Reddit API, returns titles of hot articles"""

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API.
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): List to store the titles of hot articles.
        after (str): Parameter used for pagination to get next set of results.
    Returns:
        list or None: List containing titles of all hot articles for subreddit.
        Returns None if the subreddit is invalid or no results are found.
    """
    if after is None:
        after = ''

    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    results = get(url, params=parameters, headers=user_agent,
                  allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            recurse(subreddit, hot_list, after_data)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return None
