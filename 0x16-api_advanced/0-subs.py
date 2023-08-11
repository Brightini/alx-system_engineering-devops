#!/usr/bin/python3
""" This script queries a Reddit API and returns the number of suscribers """

import requests


def number_of_subscribers(subreddit):
    """
       Defines function to get number of subscribers

       Args:
           subreddit: subreddit to be querried

       Return:
           number of subscribers, if status code is 200,
           else 0 (for invalid subreddits)
    """
    header = {'User-Agent': 'PseudoApp'}

    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/about.json', headers=header
        )

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
