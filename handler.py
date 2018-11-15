import json
import logging
import os

import requests
import telegram
import twitter

DAD_JOKE_URL = 'https://icanhazdadjoke.com/'
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')


logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)


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


api = twitter.Api(
    consumer_key=TWITTER_CONSUMER_KEY,
    consumer_secret=TWITTER_CONSUMER_SECRET,
    access_token_key=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET)


def post_to_twitter(event, context):
    """Posts to the Dad Joke Twitter bot"""
    dad_joke_api_response = _get_dad_joke()
    dad_joke_api_response_status_code = dad_joke_api_response.get('status')
    if dad_joke_api_response_status_code == 200:
        try:
            dad_joke = dad_joke_api_response.get('joke')
            api.PostUpdate(dad_joke)
            return dad_joke
        except Exception as ex:
            raise Exception(f"Unsuccessful post attempt to Twitter: {ex}")


def configure_telegram():
    """
    Configures the bot with a Telegram Token.

    Returns a bot instance.
    """
    if not TELEGRAM_TOKEN:
        logger.error('The TELEGRAM_TOKEN must be set')
        raise NotImplementedError

    return telegram.Bot(TELEGRAM_TOKEN)


OK_RESPONSE = {
    'statusCode': 200,
    'headers': {
        'Content-Type': 'application/json'
    },
    'body': 'ok'
}

ERROR_RESPONSE = {
    'statusCode': 400,
    'body': 'Oops, something went wrong!'
}

DEFAULT_MESSAGE = "Hello, I'm Tata Jokes Bot and I love to tell great Dad jokes."\
                  " My commands are: joke - to hear a classic worthy of any"\
                  " Christmas cracker."
ERROR_MESSAGE = "Oops, something went wrong. I've already informed my creator."
UNKNOWN_COMMAND = "Sorry, I didn't understand that. Commands I understand: joke / help."


def webhook(event, context):
    """
    Runs the Telegram webhook.
    """

    bot = configure_telegram()
    logger.info(f'webhook event: {event}')
    logger.info(f'webhook context: {context}')

    if event.get('httpMethod') == 'POST' and event.get('body'):
        logger.info('Message received')
        update = telegram.Update.de_json(json.loads(event.get('body')), bot)
        chat_id = update.message.chat.id
        received_message = update.message.text.lower()

        if received_message in ['start', 'help', 'hello']:
            send_message = DEFAULT_MESSAGE
        elif received_message == 'joke':
            dad_joke_api_response = _get_dad_joke()
            dad_joke_api_response_status_code = dad_joke_api_response.get(
                'status')
            if dad_joke_api_response_status_code == 200:
                send_message = dad_joke_api_response.get('joke')
            else:
                send_message = ERROR_MESSAGE
        else:
            send_message = UNKNOWN_COMMAND

        try:
            bot.sendMessage(chat_id=chat_id, text=send_message)
            logger.info('Message sent')
        except Exception as ex:
            raise Exception(f"Unsuccessful post attempt to Telegram: {ex}")

        return OK_RESPONSE

    return ERROR_RESPONSE


def set_webhook(event, context):
    """
    Sets the Telegram bot webhook.
    """

    logger.info('set_webhook event: f{event}')
    logger.info(f'set_webhook context: {context}')
    bot = configure_telegram()
    host = event.get('headers').get('Host')
    stage = event.get('requestContext').get('stage')
    url = f'https://{host}/{stage}/'
    webhook = bot.set_webhook(url)

    if webhook:
        return OK_RESPONSE

    return ERROR_RESPONSE
