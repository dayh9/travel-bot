from enum import Enum


class HotelList(Enum):
    LOCATION = "$location "

    CHECKIN = "$check in "
    CHECKOUT = "$check out "

    ADULTS1 = "$adults "
    CHILDREN1 = "$children "

    STARRATINGS = "$star rating "

    PRICEMIN = "$price min "
    PRICEMAX = "$price max "

    SORTORDER = "$sort "

    GUESTRATINGMINIMUM = "$ guest rating min "



class HotelDetails(Enum):
    CHECKIN = "$check in "
    CHECKOUT = "$check out "

    ADULTS1 = "$adults "
    CHILDREN1 = "$children "
