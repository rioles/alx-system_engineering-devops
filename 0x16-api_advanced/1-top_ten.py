#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        print(None)
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
