#!/usr/bin/python3
"""

querying the reddit API and returning the number of the total subscribers
for a given subreddit. If invalid, the function will return 0.

""" 

import requests 

def number_of_subscribers(subreddit):
	"""querying the Reddit API"""

	headers = { 
		"User-Agent": "0x16 API Advanced"
	}

	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	response = requests.get(url, headers=headers, allow_redirects = False)
	if response.status_code != 200: 
		print("No subreddit")
		return 0 
	sub = response.json().get("data").get("subscribers")
	return sub 

