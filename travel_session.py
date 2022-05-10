import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_KEY_TRAVEL = os.getenv("RAPIDAPI_KEY_TRAVEL")
TRAVEL_PAYOUTS_KEY = os.getenv("TRAVEL_PAYOUTS_KEY")


class TravelSession:
    def __init__(
        self,
        location=None,
        destination_id=None,
        currency="EUR",
        querystring=None,
        departureAirport=None,
    ):
        self.location = location
        self.destination_id = destination_id
        self.querystring = querystring
        self.currency = currency
        self.departureAirport = departureAirport

    def get_airport_by_location_name(self):
        url = "https://aerodatabox.p.rapidapi.com/airports/search/term"

        querystring = {"q": self.departureAirport, "limit": "10"}

        headers = {
            "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com",
            "X-RapidAPI-Key": RAPIDAPI_KEY_TRAVEL,
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)

        airport_code = data["items"][0]["iata"]
        print(airport_code)

    def get_flight_data(self):
        url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"

        querystring = {
            "origin": self.departureAirport,
            "destination": self.location,
            "departure_at": "2022-07",
            "return_at": "2022-08",
            "unique": "false",
            "sorting": "price",
            "direct": "false",
            "currency": "pln",
            "limit": "30",
            "page": "1",
            "one_way": "true",
            "token": TRAVELPAYOUTS_KEY,
        }

        response = requests.request("GET", url, params=querystring)
        data = json.loads(response.text)

        flight_number = data["data"][0]["flight_number"]
        departure_at = data["data"][0]["departure_at"]
        airline = data["data"][0]["airline"]
        price = data["data"][0]["price"]

        print(flight_number)
        print(departure_at)
        print(airline)
        print(price)

    def get_name_and_destination_id(self):

        url = "https://hotels4.p.rapidapi.com/locations/v2/search"

        querystring = {"query": self.location, "currency": self.currency}

        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "hotels4.p.rapidapi.com",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)

        destination_id = data["suggestions"][0]["entities"][0]["destinationId"]
        name = data["suggestions"][0]["entities"][0]["name"]

        self.destination_id = destination_id
        return name, destination_id

    def get_hotels_for_destination_id(self):
        if not self.destination_id:
            return "Please provide location for hotels to be found!"

        url = "https://hotels4.p.rapidapi.com/properties/list"

        querystring = {
            "destinationId": self.destination_id,
            "pageNumber": "1",
            "pageSize": "25",
            "checkIn": "2022-04-02",  # boilerplate data
            "checkOut": "2022-04-09",
            "currency": self.currency,
        }

        for key, value in self.querystring.items():
            querystring[key] = value

        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "hotels4.p.rapidapi.com",
        }

        print(f"before request {str(querystring)}")
        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)
        new_message = f"""{data["data"]["body"]["header"]} 
        Proponowany hotel:
        {data["data"]["body"]["searchResults"]["results"][0]["name"]}
        """
        # Adres:
        # {data["data"]["body"]["searchResults"]["results"][0]["address"]["streetAddress"]}

        return new_message

    def add_to_querysting(self, parameter, value):
        if not self.querystring:
            self.querystring = {}

        self.querystring.update({parameter: str(value)})

        return str(self.querystring)
