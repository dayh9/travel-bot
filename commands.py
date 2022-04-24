from enum import Enum


class SessionList(str, Enum):
    START = "$start"
    CLOSE = "$close"
    ADD_GUEST = "$add guest "


class SessionListDesc(str, Enum):
    START = " -> start new session"
    CLOSE = " -> close current session"
    ADD_GUEST = " -> add guest to your session"


class HotelList(str, Enum):
    HELP = "$help"
    CLEAR = "$clear"

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
    HELP = " -> show possible commands"
    CLEAR = " -> clear filters for hotels"

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


class HotelDetails(str, Enum):
    CHECK_IN = "$check in "
    CHECK_OUT = "$check out "

    ADULTS = "$adults "
    CHILDREN = "$children "
