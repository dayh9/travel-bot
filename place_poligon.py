import json
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


def get_location():

    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {"query": "new york", "locale": "en_US", "currency": "USD"}

    headers = {
        "x-rapidapi-key": "b2ee8b9a9bmsha914e6e2a4365bcp1874a7jsnffbe7af0cc2d",
        "x-rapidapi-host": "hotels4.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)

    print(data["term"])
    print(data["suggestions"][0]["entities"][0]["destinationId"])

    # print(response.text)


def get_location_hotels():
    url = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {
        "destinationId": "1506246",
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
        "x-rapidapi-key": "b2ee8b9a9bmsha914e6e2a4365bcp1874a7jsnffbe7af0cc2d",
        "x-rapidapi-host": "hotels4.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    print(data["data"]["body"]["header"])
    print("Proponowany hotel")
    print(data["data"]["body"]["searchResults"]["results"][0]["name"])
    print(
        data["data"]["body"]["searchResults"]["results"][0]["address"]["streetAddress"]
    )

    # print(response.text)
