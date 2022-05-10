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

    def get_airport_by_location_name(self, location):
        url = "https://aerodatabox.p.rapidapi.com/airports/search/term"

        querystring = {"q": location, "limit": "10"}

        headers = {
            "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com",
            "X-RapidAPI-Key": RAPIDAPI_KEY_TRAVEL,
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)

        airport_code = data["items"][0]["iata"]
        self.departureAirport
        return airport_code

    def get_flight_data(self):
        url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"

        today = date.today()
        departureAt = today.strftime("%Y-%m-%d")
        returnAt = (today + timedelta(days=DEFAULT_SESSION_DURATION_DAYS)).strftime(
            "%Y-%m-%d"
        )

        querystring = {
            "origin": self.departureAirport,
            "destination": self.location,
            "departure_at": departureAt,
            "return_at": returnAt,
            "unique": "false",
            "sorting": "price",
            "direct": "false",
            "currency": "eur",
            "limit": "30",
            "page": "1",
            "one_way": "true",
            "token": TRAVEL_PAYOUTS_KEY,
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

    def add_to_querysting(self, parameter, value):
        if not self.querystring:
            self.querystring = {}

        self.querystring.update({parameter: str(value)})

        return str(self.querystring)
