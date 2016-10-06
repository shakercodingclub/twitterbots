import tweepy
import time  # To use time.sleep()
import os  # For accessing file system

CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
oauth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(oauth)

# This is the file path of the text file being read
text_path = os.path.dirname(os.path.realpath(__file__)) + '\\tweet_this.txt'

# Opens the file ('r' stands for 'read')
text_file = open(text_path, 'r')

# Saves the the text file's text to a string variable called 'text'
text = text_file.read()

split_text = text.split('\n')
# That line^ creates an array with each new line ('\n') of text at each index
# For example, if your text file reads:
#
# "Yolo and swag
#  blah blah blah
#  cheeseburger"
#
# Then variable split_text now contains this:
# ['Yolo and swag', 'blah blah blah', 'cheeseburger']


# Tweets a new line of your text file every 15 seconds
for tweet in split_text:
    api.update_status(tweet)
    time.sleep(15)
