#!/usr/bin/python3
'''task 0'''

import requests


def number_of_subscribers(subreddit):
    '''get number of subs from subreddit'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'}).json()
    try:
        subs = r["data"]["subscribers"]
        return subs
    except:
        return 0
