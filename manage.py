import argparse

from src.request import get_dad_joke


def cli():
    """For local development"""

    parser = argparse.ArgumentParser(description="Local dev CLI")
    parser.add_argument(
        "-j", "--joke", help="Tell me a Dad joke", action="store_true")

    args = parser.parse_args()

    if args.joke:
        response = get_dad_joke()
        joke = response.get('joke')
        print(f'\n{joke}\n')


if __name__ == "__main__":
    cli()
