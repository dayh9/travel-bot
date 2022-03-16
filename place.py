import os

import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def get_place():
    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {"query": "warsaw", "locale": "en_US", "currency": "PLN"}

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "hotels4.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    print(data)
