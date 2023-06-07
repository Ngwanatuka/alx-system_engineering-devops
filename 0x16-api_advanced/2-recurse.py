#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and
returns a list containing the titles of all all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None, max_iterations=10):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Customer User Agent'}
    params = {'limit': 100}  # Maximum number of posts per request

    if after:
        params['after'] = after

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                if 'data' in post and 'title' in post['data']:
                    hot_list.append(post['data']['title'])
        if 'data' in data and 'after' in data['data']:
            after = data['data']['after']
            if len(hot_list) < max_iterations * 100:
                return recurse(subreddit, hot_list, after, max_iterations)
            else:
                return hot_list
        else:
            return hot_list
    except (requests.exceptions.RequestException, ValueError, KeyError):
        return None
