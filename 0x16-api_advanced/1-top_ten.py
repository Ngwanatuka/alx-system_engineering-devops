#!/usr/bin/python3
"""
a script that prints the title of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            for post in posts[:10]:
                print(post['data']['title'])
        except KeyError:
            print("None")
    else:
        print("None")
