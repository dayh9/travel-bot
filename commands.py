from enum import Enum


class SessionList(str, Enum):
    START = "$start"
    CLOSE = "$close"
    HELP = "$help"
    CLEAR = "$clear"


class SessionListDesc(str, Enum):
    START = " -> start new session"
    CLOSE = " -> close current session"
    HELP = " -> show possible commands"
    CLEAR = " -> clear all filters"


class HotelList(str, Enum):
    LOCATION = "$location "
    HOTELS = "$hotels"

    CHECK_IN = "$check in "
    CHECK_OUT = "$check out "

    ADULTS = "$adults "
    CHILDREN = "$children "

    STAR_RATINGS = "$star rating "

    PRICE_MIN = "$price min "
    PRICE_MAX = "$price max "

    SORT_ORDER = "$sort "

    GUEST_RATING_MINIMUM = "$guest rating min "


class HotelListDesc(str, Enum):
    LOCATION = "<value> -> provide location for your next journey [string]"
    HOTELS = " -> run to list hotels in the location"

    CHECK_IN = "<value> -> provide check in date [format: YYYY-MM-DD]"
    CHECK_OUT = "<value> -> provide check out date [format: YYYY-MM-DD]"

    ADULTS = "<value> -> provide number of adults to accomodate [number]"
    CHILDREN = "<value> -> provide number of children to accomodate [number]"

    STAR_RATINGS = '<values> -> provide star rating [values separated with ",": 2,4,5]'

    PRICE_MIN = "<value> -> provide price min [number]"
    PRICE_MAX = "<value> -> provide price max [number]"

    SORT_ORDER = "<value> -> provide sort option [one of: BEST_SELLER, STAR_RATING_HIGHEST_FIRST, STAR_RATING_LOWEST_FIRST, DISTANCE_FROM_LANDMARK, GUEST_RATING, PRICE_HIGHEST_FIRST, PRICE"

    GUEST_RATING_MINIMUM = "<value> -> guest rating min [number]"


class TravelList(str, Enum):
    AIRPORT_ORIGIN = "$airport origin "
    AIRPORT_DESTINATION = "$airport destination "
    FLIGHT_DEPARTURE_DATE = "$flight departure "
    FLIGHT_RETURN_DATE = "$flight return "
    FLIGHTS = "$flights"


class TravelListDesc(str, Enum):
    AIRPORT_ORIGIN = "<value> -> provide location for origin airport [string]"
    AIRPORT_DESTINATION = "<value> -> provide location for destination airport [string]"
    FLIGHT_DEPARTURE_DATE = (
        "<value> -> provide flight departure date [format: YYYY-MM-DD]"
    )
    FLIGHT_RETURNAT_DATE = "<value> -> provide flight return date [format: YYYY-MM-DD]"
    FLIGHTS = " -> show list of possible flights"
