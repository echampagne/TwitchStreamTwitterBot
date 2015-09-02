#!/usr/bin/python

import urllib2
# from urllib2 import Request
from urllib2 import URLError
import json

# Returns a tuple of the form (Online, URLofStream)
# is URL None if offline.
def get_info(user):
	# tweet = {}
	url = 'https://api.twitch.tv/kraken/streams/' + user
	try:
		info = json.loads(urllib2.urlopen(url, timeout=15).read().decode('utf-8'))
		if info['stream'] == None:
			return (False, None)
		else:
			return (True, info['stream']['channel']['url'])
	except URLError as e:
		# Not found or some other error.
		# Either way, the user entered stream is not alive
		return (False, None)


def twitter_info_setup(config_file="config.txt"):
	bot_config = {}
	required_fields = ["CONSUMER_KEY", "CONSUMER_SECRET",
						"ACCESS_KEY", "ACCESS_SECRET"]

	with open(config_file, "r") as file:
		for line in file:
			line = line.split(":")
			variable = line[0].strip()
			value = line[1].strip()
			bot_config[variable] = value
	# Check to make sure all required fields are in the config file
	if not all(field in bot_config for field in required_fields):
		return None
	return bot_config


