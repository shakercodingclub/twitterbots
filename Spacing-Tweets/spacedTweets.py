import tweepy
import time  # We'll use this to space out our tweets

CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
oauth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(oauth)

# The code below will make 10 tweets spaced 60 seconds apart in the format: 
# "This is my 1st automated tweet!"

num_suffix = ['st', 'nd', 'rd', 'th']  # 1st, 2nd, 3rd, 4th, 5th...
for i in range(1, 11):  # Loops 10 times
    message = "This is my " + str(i)
    if i < 4:  # If this is the first, second or third loop...
        message += num_suffix[i-1]  # Use a unique suffix ('st', 'nd', rd')
    else:
        message += num_suffix[3]  # Use the typical suffix ('th')
    message += ' automated tweet!'

    api.update_status(message)  # Update Twitter status with rad message

    time.sleep(60)  # Wait 60 seconds before proceeding
