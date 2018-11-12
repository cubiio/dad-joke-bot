import json

import requests

DAD_JOKE_URL = 'https://icanhazdadjoke.com/'


def get_dad_joke():
    """Makes requests to the Dad joke API"""
    headers = {
        "Accept": "application/json",
        # TODO(sam) add user agent info
        "User-Agent": ""
    }
    try:
        request = requests.get(DAD_JOKE_URL, headers=headers)
        response = json.loads(request.text)
        return response
    except Exception as ex:
        raise Exception(f"Unsuccessful request to {DAD_JOKE_URL}: {ex}")
