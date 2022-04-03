import json
import os

import requests
from dotenv import load_dotenv
from requests.exceptions import HTTPError

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


class HotelSession:
    def __init__(
        self,
        location=None,
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

    def set_location_and_destination_id(self, location):

        url = "https://hotels4.p.rapidapi.com/locations/v2/search"
        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "hotels4.p.rapidapi.com",
        }
        querystring = {"query": location, "currency": self.currency}

        success, data = self._send_request(url, headers, querystring)
        # response = requests.request("GET", url, headers=headers, params=querystring)
        # data = json.loads(response.text)

        if not success:
            return data, None

        destination_id = data["suggestions"][0]["entities"][0]["destinationId"]
        name = data["suggestions"][0]["entities"][0]["name"]

        self.location = name
        self.destination_id = destination_id
        return name, destination_id

    def get_hotels_for_destination_id(self):
        if not self.destination_id:
            return "Please provide location for hotels to be found!"

        url = "https://hotels4.p.rapidapi.com/properties/list"
        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "hotels4.p.rapidapi.com",
        }

        # TODO: VALIDACJA parametrow dodac
        querystring = {
            "destinationId": self.destination_id,
            "pageNumber": "1",
            "pageSize": "25",
            "checkIn": "2022-04-05",  # boilerplate data TODO: sciaganie daty
            "checkOut": "2022-04-10",
            "currency": self.currency,
        }
        if self.querystring:
            for key, value in self.querystring.items():
                querystring[key] = value

        # print(f"before request {str(querystring)}")
        # response = requests.request("GET", url, headers=headers, params=querystring)

        success, data = self._send_request(url, headers, querystring)

        if not success:
            return data

        return self._prepare_hotels_response(data)

    def add_to_querysting(self, parameter, value):
        if not self.querystring:
            self.querystring = {}

        self.querystring.update({parameter: str(value)})

        return str(self.querystring)

    def _send_request(self, url, headers, querystring):
        try:
            print(f"request url={url},\nquerystring={querystring}")
            response = requests.get(url, headers=headers, params=querystring)
            print(f"response: {str(response.text)}")
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            return False, f"HTTP error occurred: {http_err}"
        except Exception as err:
            return False, f"Other error occurred: {err}"
        else:
            return True, json.loads(response.text)

    def _prepare_hotels_response(self, data):
        if data["data"]["body"]["searchResults"]["results"]:
            new_message = f"""{data["data"]["body"]["header"]}
            Proponowany hotel:
            {data["data"]["body"]["searchResults"]["results"][0]["name"]}
            """
            # Adres:
            # {data["data"]["body"]["searchResults"]["results"][0]["address"]["streetAddress"]}

        else:
            new_message = "No results found"
        return new_message
