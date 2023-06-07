#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and
returns a list containing the titles of all all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if posts:
            hot_list.extend([post["data"]["title"] for post in posts])
            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list, after)

    return hot_list if hot_list else None
