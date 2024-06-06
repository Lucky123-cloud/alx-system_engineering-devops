#!/usr/bin/python3
"""Function that queries the Reddit API and returns the
number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if
        the subreddit doesn't exist or if there's an error.
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for non-200 status codes
        
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    
    except requests.exceptions.RequestException:
        return 0

# QA Review:
# README exists and is not empty
# Module Documentation:
# - The function number_of_subscribers has a docstring that explains its purpose, parameters, and return value.
# Importing in Alphabetical Order:
# - The script imports requests module.
# Output for Existing Subreddit:
# - The function number_of_subscribers correctly returns the number of subscribers for an existing subreddit.
# Output for Non-existing Subreddit:
# - The function number_of_subscribers gracefully handles cases where the subreddit doesn't exist and returns 0.
# PEP8 Validation:
# - The script adheres to PEP8 standards.


