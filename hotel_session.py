import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


class HotelSession:
    def __init__(
        self,
        location,
        destination_id=None,
        currency="EUR",
        querystring=None
        # check_in=None,
        # check_out=None,
        # adults=None,
        # children=None,
        # star_ratings=None,
        # price_min=None,
        # price_max=None,
        # sort_order=None,
        # guest_rating_minimum=None,
        # amenity_id=None,
        # hotels_list=None,
    ):
        self.location = location
        self.destination_id = destination_id
        self.querystring = querystring
        self.currency = currency
        # self.check_in = check_in
        # self.check_out = check_out
        # self.adults = adults
        # self.children = children
        # self.star_ratings = star_ratings
        # self.price_min = price_min
        # self.price_max = price_max
        # self.sort_order = sort_order
        # self.guest_rating_minimum = guest_rating_minimum
        # self.amenity_id = amenity_id
        # self.hotels_list = hotels_list

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
