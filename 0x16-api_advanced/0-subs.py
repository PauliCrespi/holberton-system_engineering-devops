#!/usr/bin/python3
"""task 0"""
import requests


def number_of_subscribers(subreddit):
    """number of suscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    cont = '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    cont2 = ' (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    user_agent = {'User-agent': 'Mozilla/5.0 {}{}'.format(cont, cont2)}
    response = requests.get(url, headers=user_agent)

    if response.status_code != 200:
        return 0
    else:
        return response.json().get("data").get("suscribers")
