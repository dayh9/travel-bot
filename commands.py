from enum import Enum


class HotelList(Enum):
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

    GUEST_RATING_MINIMUM = "$ guest rating min "


class HotelDetails(Enum):
    CHECK_IN = "$check in "
    CHECK_OUT = "$check out "

    ADULTS = "$adults "
    CHILDREN = "$children "
