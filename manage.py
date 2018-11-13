import argparse

from src.joke_request import get_dad_joke
from src.twitter_bot import twitter_bot_post_joke


def cli():
    """For local development"""

    parser = argparse.ArgumentParser(description="Local dev CLI")
    parser.add_argument(
        "-j", "--joke", help="Tell me a Dad joke", action="store_true")
    parser.add_argument(
        "-t",
        "--twitter",
        help="Post a Dad joke to the Twitter bot",
        action="store_true")

    args = parser.parse_args()

    if args.joke:
        response = get_dad_joke()
        joke = response.get('joke')
        print(response)
        print(f'\n{joke}\n')
    if args.twitter:
        dad_joke_api_response = get_dad_joke()
        dad_joke = dad_joke_api_response.get('joke')
        twitter_request = twitter_bot_post_joke(dad_joke)
        print(f'\nPosted Dad joke to Twitter:\n{dad_joke}\n')
        print(f'\nTwitter response:\n{twitter_request}\n')


if __name__ == "__main__":
    cli()
