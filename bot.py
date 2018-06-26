'''
based on https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/
'''
import tweepy, time, sys, credentials, utils, text_generators
'''
credentials and utils are .py files in the local directory. 

credentials contains dictionaries for keys and secrets. 
This file is not include in the git repo for security

Utils contains helper functions
'''

CONSUMER_KEY = credentials.keys['CONSUMER_KEY']
ACCESS_KEY = credentials.keys['ACCESS_KEY']
CONSUMER_SECRET = credentials.secrets['CONSUMER_SECRET']
ACCESS_SECRET = credentials.secrets['ACCESS_SECRET']

#INTERVAL = 60 * 60 * 6  # tweet every 6 hours
INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

counter = 1
while True:
	utils.print_flush("about to get status...\n")
	status = text_generators.hello_twitter(counter)
	utils.print_flush(status)
	api.update_status(status)
	counter += 1
	time.sleep(INTERVAL)
