import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def _get_destination_id(location):

    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {"query": location, "locale": "en_US", "currency": "USD"}

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "hotels4.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)

    print(data["term"])
    destination_id = data["suggestions"][0]["entities"][0]["destinationId"]
    return destination_id


def get_hotels_for_location(location):

    destination_id = _get_destination_id(location)

    url = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {
        "destinationId": destination_id,
        "pageNumber": "1",
        "pageSize": "25",
        "checkIn": "2020-01-08",
        "checkOut": "2020-01-15",
        "adults1": "1",
        "sortOrder": "PRICE",
        "locale": "en_US",
        "currency": "USD",
    }

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "hotels4.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    new_message = f"""{data["data"]["body"]["header"]} 
    Proponowany hotel:
    {data["data"]["body"]["searchResults"]["results"][0]["name"]}
    Adres:
    {data["data"]["body"]["searchResults"]["results"][0]["address"]["streetAddress"]}
    """

    print(data["data"]["body"]["header"])
    print("Proponowany hotel")
    print(data["data"]["body"]["searchResults"]["results"][0]["name"])
    print(
        data["data"]["body"]["searchResults"]["results"][0]["address"]["streetAddress"]
    )

    return new_message
