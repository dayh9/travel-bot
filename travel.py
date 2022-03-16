import os

import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def get_sth():
    url = "https://priceline-com-provider.p.rapidapi.com/v2/flight/autoComplete"

    querystring = {
        "string": "Wroclaw",
        "pois": "true",
        "hotels": "true",
        "airports": "true",
        "cities": "true",
        "regions": "true",
    }

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "priceline-com-provider.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
