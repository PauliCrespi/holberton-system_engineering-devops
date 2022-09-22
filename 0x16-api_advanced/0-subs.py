#!/usr/bin/python3
"""task 0"""
import requests


def number_of_subscribers(subreddit):
    """number of suscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = requests.get(url, headers = user_agent)

    if response.status_code != 200:
        return 0
    else:
        return response.json().get("data").get("suscribers")
