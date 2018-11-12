import argparse

from src.request import get_dad_joke
from src.twitter_bot import post_to_twitter


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
        print(f'\n{joke}\n')
    if args.twitter:
        response = post_to_twitter()
        joke = response.get('joke')
        print(f'\nPosted Dad joke to Twitter:\n{joke}\n')


if __name__ == "__main__":
    cli()
