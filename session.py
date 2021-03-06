from hotel_session import HotelSession
from travel_session import TravelSession

class Session:
    def __init__(self, user, channel_id):
        self.user = user
        self.channel_id = channel_id
        self.guests = []
        self.hotel_session = HotelSession()  # possibility of adding multiple sessions
        self.travel_session = TravelSession()

    def is_valid_user(self, user_id):
        valid_users = [self.user] + self.guests
        if user_id in valid_users:
            return True
        return False

    def add_guest(self, guest):
        if not guest in self.guests:
            self.guests.append(guest)
