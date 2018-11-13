from src.joke_request import get_dad_joke
from src.twitter_bot import twitter_bot_post_joke


def post_to_twitter(event, context):
    """Posts to the Dad Joke Twitter bot"""
    dad_joke_api_response = get_dad_joke()
    dad_joke_api_response_status_code = dad_joke_api_response.get('status')
    if dad_joke_api_response_status_code == 200:
        try:
            dad_joke = dad_joke_api_response.get('joke')
            twitter_bot_post_joke(dad_joke)
            return dad_joke
        except Exception as ex:
            raise Exception(f"Unsuccessful post attempt to Twitter: {ex}")
