# given a user input, send a tweet
# for hashtags, type "\" before

# import statements
from twython import Twython
import sys

# variables from auth.py
from auth import(
 	consumer_key,
    	consumer_secret,
    	access_token,
	access_token_secret
)

# make connection with the Twitter API using the imported variables
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# grab message to send to Twitter as a tweet
message = " "
message = message.join(sys.argv[1:])
if len(message) <= 140:
	twitter.update_status(status=message)
	print("Tweeted: %s" %message)
else:
	print("This tweet is longer than 140 characters, please shorten it and try again.")
