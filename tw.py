import tweepy
from twython import Twython

CONSUMER_KEY = 'c50hq8BL6aqkfL76JwzKHFmNO'
CONSUMER_SECRET = '1TnC2YzUIsOlhqxThsctUsQW7YBAF1ESErVo4et8H1Hfy8Drfg'
ACCESS_TOKEN = '1219710168-wZDGLy5byKSHs7K1fl3Z9M4BWhl0BOwOtOjwFKS'
ACCESS_TOKEN_SECRET = 'MmgOxLAZ3lBZSkaMbHy3NYSpOyq8xTudIbuPBluAKfZrK'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# twitter.update_status(status="Python ile tweet atma.. :D")