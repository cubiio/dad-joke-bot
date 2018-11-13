import os

import twitter
from dotenv import load_dotenv

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


def twitter_bot_post_joke(dad_joke):
    """Posts to Dad Joke Twitter bot @tata_jokes

    Parameters
    ----------
        dad_joke : str
            response from the Dad Joke API

    Returns
    -------
    JSON object | Exception
        Response object from Twitter API
    """
    try:
        twitter_request = api.PostUpdate(dad_joke)
        return twitter_request
    except Exception as ex:
        raise Exception(f"Unsuccessful post attempt to Twitter: {ex}")
