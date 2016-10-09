#!/usr/bin/python3.5
import tweepy
import time
import os

def numTate(letter):  # The lazy way
    if letter == 'A':
        return 'B'
    elif letter == 'B':
        return 'C'
    elif letter == 'C':
        return 'D'
    else:
        return 'A'

CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
oauth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(oauth)

text_path = os.path.dirname(os.path.realpath(__file__)) + '/rotation_schedule.txt'
text_file = open(text_path, 'r')
text = text_file.read()
lines = text.split('\n')

current_date = time.strftime("%m/%d/%y")
lookup_table = []

last_line = []
for line in lines:
    lookup = line.split('\t')
    if lookup[0] == current_date:
        message = "Today's rotation schedule: "
        p8 = int(lookup[3])
        if p8 != 0:
            current_letter = lookup[4]
            for period in range(1, 8):
                if period == p8:
                    message += '8' + current_letter + ' '
                    current_letter = numTate(current_letter)
                else:
                    message += str(period) + current_letter + ' '
        else:
            current_letter = numTate(last_line[4])
            for period in range(1, 8):
                message += str(period) + current_letter + ' '
        api.update_status(message)
        print(message)
    else:
        last_line = lookup
print('end')
