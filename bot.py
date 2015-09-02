#!/usr/bin/env/python

import tweepy, time, sys, bot_utils

# Twitter OAuth
config_file="config.txt"
twitter_info = bot_utils.twitter_info_setup(config_file)
if twitter_info:
	auth = tweepy.OAuthHandler(twitter_info["CONSUMER_KEY"], twitter_info["CONSUMER_SECRET"])
	auth.set_access_token(twitter_info["ACCESS_KEY"], twitter_info["ACCESS_SECRET"])
	api = tweepy.API(auth)
else:
	print "Please fill out the config.txt file"

info = bot_utils.get_info(twitter_info["USER"])
# info of form(Online, URL)
if info[0]:
	api.update_status(status="%s's twitch stream is now live! Link: %s" % (twitter_info["USER"], info[1]))
