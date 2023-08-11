#!/usr/bin/python3
""" This script queries a Reddit API and
prints the first 10 posts of a subreddit """

import requests
import json


def top_ten(subreddit):
    """
       Defines function to print first 10 posts

       Args:
           subreddit: subreddit to be querried

       Return:
           first 10 posts, if status code is 200,
           else None (for invalid subreddits)
    """
    header = {'User-Agent': 'PseudoApp'}

    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json', headers=header)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        count = 0
        for post in posts:
            if count < 10:
                title = post['data'].get('title')
                if title:
                    print(title)
                    count += 1
    else:
        print(None)
