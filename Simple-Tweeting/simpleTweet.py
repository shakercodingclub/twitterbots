import tweepy

# You can find this by going back to your twitter window and finding "Consumer Key (API Key)
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

# You can find this by clicking "manage keys and access tokens" and finding "Consumer Secret (API Secret)"
# This is a "secret" key. While it should never be "human-readable" in your application for security
# reasons, copying and pasting it here is okay for our purposes.
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Scroll down and click "Create my access token", if you haven't already.

# This is right next to "Access Token"
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# This is right next to "Access Token Secret"
# Just like CONSUMER_SECRET, this is a "secret" token. Same notes apply.
ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# If you're wondering what all these "Keys" and "Tokens" are for, Twitter makes use of OAuth for secure
# authorization and log-ins (like what we're about to do). It's a bit complicated, but that's expected.
# Youtuber Tom Scott has a quick explanation of OAuth in his "Pokemon Go" video (link below)
# https://www.youtube.com/watch?v=cDZjm4f9CEo

# For the nerds, documentation on the Tweepy module can be found at http://docs.tweepy.org/en/v3.5.0/api.html
oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
oauth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(oauth)

# I update your Twitter status!
api.update_status('Coding club rules!')  # It does.
