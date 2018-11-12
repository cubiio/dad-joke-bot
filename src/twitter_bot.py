import os

import twitter
from dotenv import load_dotenv

from src.request import get_dad_joke

load_dotenv()

TWITTER_CONSUMER_KEY = os.getenv('api_key')
TWITTER_CONSUMER_SECRET = os.getenv('api_secret_key')
ACCESS_TOKEN = os.getenv('access_token')
ACCESS_TOKEN_SECRET = os.getenv('access_token_secret')

api = twitter.Api(
    consumer_key=TWITTER_CONSUMER_KEY,
    consumer_secret=TWITTER_CONSUMER_SECRET,
    access_token_key=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET)


def post_to_twitter():
    """Posts to the Dad Joke Twitter bot"""
    response = get_dad_joke()
    if response.get('status') == 200:
        dad_joke = response.get('joke')
        api.PostUpdate(dad_joke)
        return response
