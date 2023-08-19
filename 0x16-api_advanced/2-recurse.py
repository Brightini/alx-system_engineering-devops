#!/usr/bin/python3
""" This script queries a Reddit API and
returns a list containing the titles of all hot
articles for a given subreddit """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
       Defines function to query a Reddit API

       Args:
           subreddit: subreddit to be querried

       Return:
           a list containing the titles of all hot articles
           else None (for invalid subreddits or no results)
    """
    header = {'User-Agent': 'PseudoApp'}
    param = {'after': after} if after else None

    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json',
        headers=header,
        params=param
        )

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data'].get('title')
            hot_list.append(title)

        if data['data']['after']:
            new_after = data['data']['after']
            return recurse(subreddit, hot_list, after=new_after)
        else:
            return hot_list
    else:
        return None
