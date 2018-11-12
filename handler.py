import json
import os

import requests
import twitter
from dotenv import load_dotenv


load_dotenv()

TWITTER_CONSUMER_KEY = os.getenv('api_key')
TWITTER_CONSUMER_SECRET = os.getenv('api_secret_key')
ACCESS_TOKEN = os.getenv('access_token')
ACCESS_TOKEN_SECRET = os.getenv('access_token_secret')
DAD_JOKE_URL = 'https://icanhazdadjoke.com/'


api = twitter.Api(
    consumer_key=TWITTER_CONSUMER_KEY,
    consumer_secret=TWITTER_CONSUMER_SECRET,
    access_token_key=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET)


def _get_dad_joke():
    """Makes requests to the Dad joke API"""
    headers = {
        "Accept":
        "application/json",
        "user-agent":
        "Twitter Bot - GitHub repo https://github.com/cubiio/dad-joke-bot"
    }
    try:
        request = requests.get(DAD_JOKE_URL, headers=headers)
        response = json.loads(request.text)
        return response
    except Exception as ex:
        raise Exception(f"Unsuccessful request to {DAD_JOKE_URL}: {ex}")


def post_to_twitter(event, context):
    """Posts to the Dad Joke Twitter bot"""
    response = _get_dad_joke()
    if response.get('status') == 200:
        try:
            dad_joke = response.get('joke')
            api.PostUpdate(dad_joke)
            return response
        except Exception as ex:
            raise Exception(f"Unsuccessful post attempt to Twitter: {ex}")
