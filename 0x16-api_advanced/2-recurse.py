#!/usr/bin/python3
'''task 2'''

import requests


def recurse(subreddit, hot_list=[], pos=0):
    '''append hottest posts to hot_list'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'},
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    if pos == (len(r.json()['data']['children']) - 1):
        return pos
    hot_list.append(r.json()['data']['children'][pos])
    pos += 1
    recurse(subreddit, hot_list, pos)
