import os
import datetime

from twitter import *

CONSUMER_KEY = "###"
CONSUMER_SECRET = "###"
MY_TWITTER_CREDS = os.path.expanduser('~/.unfollower_creds')

end_date = datetime.datetime(2014, 10, 1)

if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("Unfollower", CONSUMER_KEY, CONSUMER_SECRET,
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

twitter = Twitter(auth=OAuth(
    oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

following = twitter.friends.ids()

for userid in following['ids']:
    info = twitter.users.show(id=userid)
    try:
        last_tweet = datetime.datetime.strptime(info['status']['created_at'], "%a %b %d %H:%M:%S +0000 %Y")
    except KeyError:
        print("error")
        print(info['name'])
    
    if last_tweet < end_date:
        print(info['name'])
        print(last_tweet)