import json
import os
from datetime import date, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_KEY_TRAVEL = os.getenv("RAPIDAPI_KEY_TRAVEL")
TRAVEL_PAYOUTS_KEY = os.getenv("TRAVEL_PAYOUTS_KEY")
DEFAULT_SESSION_DURATION_DAYS = 7


class TravelSession:
    def __init__(
        self,
        origin_location=None,
        destination_location=None,
        destination_id=None,
        currency="EUR",
        querystring=None,
        origin_airport=None,
        destination_airport=None,
    ):
        self.origin_location = origin_location
        self.destination_location = destination_location
        self.destination_id = destination_id
        self.querystring = querystring
        self.currency = currency
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport

    def get_airport_by_location_name(self, location):
        url = "https://aerodatabox.p.rapidapi.com/airports/search/term"

        querystring = {"q": location, "limit": "10"}

        headers = {
            "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com",
            "X-RapidAPI-Key": RAPIDAPI_KEY_TRAVEL,
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        name = data["items"][0]["name"]
        airport_code = data["items"][0]["iata"]

        self.location = name
        self.departureAirport = airport_code
        return name, airport_code

    def set_origin(self, name, code):
        self.origin_location = name
        self.origin_airport = code

    def set_destination(self, name, code):
        self.destination_location = name
        self.destination_airport = code

    def get_flight_data(self):
        if not self.origin_airport:
            return "Please provide origin airport for flights to be found!"
        if not self.destination_airport:
            return "Please provide destination airport for flights to be found!"

        url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"

        today = date.today()
        departure_at = today.strftime("%Y-%m-%d")
        return_at = (today + timedelta(days=DEFAULT_SESSION_DURATION_DAYS)).strftime(
            "%Y-%m-%d"
        )

        querystring = {
            "origin": self.origin_airport,
            "destination": self.destination_airport,
            "departure_at": departure_at,
            "return_at": return_at,
            "unique": "false",
            "sorting": "price",
            "direct": "false",
            "currency": self.currency,
            "limit": "30",
            "page": "1",
            "one_way": "false",
            "token": TRAVEL_PAYOUTS_KEY,
        }
        if self.querystring:
            for key, value in self.querystring.items():
                querystring[key] = value

        response = requests.request("GET", url, params=querystring)
        data = json.loads(response.text)
        print(data)
        flights = f"Found flights from {self.origin_location} to {self.destination_location}:\n"
        for flight in data["data"]:
            flight_number = flight["flight_number"]
            departure_at = flight["departure_at"]
            airline = flight["airline"]
            price = flight["price"]

            flights += f"number: {flight_number}, departure at: {departure_at}, return at: {return_at}, airline: {airline}, price: {price}eur\n"

        return flights

    def add_to_querysting(self, parameter, value):
        if not self.querystring:
            self.querystring = {}

        self.querystring.update({parameter: str(value)})

        return str(self.querystring)
