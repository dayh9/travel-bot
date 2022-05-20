import os
from html import unescape

import discord
from dotenv import load_dotenv

from commands import (
    HotelDetails,
    HotelList,
    HotelListDesc,
    TravelList,
    TravelListDesc,
    SessionList,
    SessionListDesc,
)
from session import Session

load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")


class MyClient(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.sessions = []

    def _get_session(self, channel_id):
        session = [s for s in self.sessions if s.channel_id == channel_id]
        if len(session) > 0:
            return session[0]
        return None

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author.id}: {0.content}; {0.channel.id}".format(message))

        author = message.author
        session = self._get_session(message.channel.id)

        if author == client.user:
            return

        if message.content.startswith(HotelList.HELP):
            commands = [c for c in zip(SessionList, SessionListDesc)]
            commands += [c for c in zip(HotelList, HotelListDesc)]
            response_message = "Possible commands: \n"
            for command in commands:
                response_message += f"{command[0].value}{command[1].value} \n"
            return await message.channel.send(response_message)

        if message.content.startswith(TravelList.HELP):
            commands = [c for c in zip(SessionList, SessionListDesc)]
            commands += [c for c in zip(TravelList, TravelListDesc)]
            response_message = "Possible commands: \n"
            for command in commands:
                response_message += f"{command[0].value}{command[1].value} \n"
            return await message.channel.send(response_message)

        if message.content.startswith(SessionList.START):
            if session:
                return await message.channel.send("Session already exists")
            else:
                new_session = Session(author.id, message.channel.id)
                self.sessions.append(new_session)
                return await message.channel.send("Session started")

        if not session:
            return await message.channel.send(
                "Session doesn't exist\nSend $start to create session"
            )

        if not session.is_valid_user(author.id):
            return await message.channel.send(
                f"""User {author} is not a guest of this session.\n
                Ask session owner for permission (this user must react to your message)"""
            )

        if message.content.startswith(SessionList.CLOSE):
            self.sessions.pop(self.sessions.index(session))
            return await message.channel.send("Session closed")

        ### Add commands only past this point

        if message.content.startswith(HotelList.CLEAR):
            session.hotel_session.querystring = None
            return await message.channel.send("Filters cleaned")

        if message.content.startswith(HotelList.LOCATION):
            location = message.content[len(HotelList.LOCATION) :]
            name, _ = session.hotel_session.set_location_and_destination_id(location)
            name_message = f"Location set to {name}"
            return await message.channel.send(name_message)

        if message.content.startswith(HotelList.HOTELS):
            if session.hotel_session:
                hotels = session.hotel_session.get_hotels_for_destination_id()
            else:
                hotels = "no location boilerplate"
            return await message.channel.send(hotels)

        if message.content.startswith(HotelList.ADULTS):
            adults = message.content[len(HotelList.ADULTS) :]
            response_message = session.hotel_session.add_to_querysting(
                "adults1", adults
            )
            return await message.channel.send(response_message)

        if message.content.startswith(HotelList.CHECK_IN):
            check_in = message.content[len(HotelList.CHECK_IN) :]
            response_message = session.hotel_session.add_to_querysting(
                "checkIn", check_in
            )
            return await message.channel.send(response_message)

        if message.content.startswith(HotelList.CHECK_OUT):
            check_out = message.content[len(HotelList.CHECK_OUT) :]
            response_message = session.hotel_session.add_to_querysting(
                "checkOut", check_out
            )
            return await message.channel.send(response_message)

        if message.content.startswith(HotelList.CHILDREN.value):
            children = message.content[len(HotelList.CHILDREN.value) :]
            response_message = session.hotel_session.add_to_querysting(
                "children1", children
            )
            return await message.channel.send(response_message)

        if message.content.startswith(HotelList.STAR_RATINGS):
            star_ratings = message.content[len(HotelList.STAR_RATINGS) :]
            response_message = session.hotel_session.add_to_querysting(
                "starRatings", star_ratings
            )
            return await message.channel.send(response_message)

        if message.content.startswith(HotelList.PRICE_MIN):
            price_min = message.content[len(HotelList.PRICE_MIN) :]
            response_message = session.hotel_session.add_to_querysting(
                "priceMin", price_min
            )
            return await message.channel.send(response_message)

        if message.content.startswith(HotelList.PRICE_MAX):
            price_max = message.content[len(HotelList.PRICE_MAX) :]
            response_message = session.hotel_session.add_to_querysting(
                "priceMax", price_max
            )
            return await message.channel.send(response_message)

        # BEST_SELLER, STAR_RATING_HIGHEST_FIRST, STAR_RATING_LOWEST_FIRST, DISTANCE_FROM_LANDMARK, GUEST_RATING, PRICE_HIGHEST_FIRST, PRICE
        if message.content.startswith(HotelList.SORT_ORDER):
            sort = message.content[len(HotelList.SORT_ORDER) :]
            response_message = session.hotel_session.add_to_querysting(
                "sortOrder", sort
            )
            return await message.channel.send(response_message)

        if message.content.startswith(HotelList.GUEST_RATING_MINIMUM):
            guest_rating_minimum = message.content[
                len(HotelList.GUEST_RATING_MINIMUM) :
            ]
            response_message = session.hotel_session.add_to_querysting(
                "guestRatingMin", guest_rating_minimum
            )
            return await message.channel.send(response_message)

        if message.content.startswith("$test"):

            response_message = unescape("total 155 € for 5&nbsp;nights")
            return await message.channel.send(response_message)





        if message.content.startswith(TravelList.AIRPORTORIGIN):
            location = message.content[len(TravelList.AIRPORTORIGIN) :]
            name, _ = session.travel_session.get_airport_by_location_name(location)
            name_message = f"Origin airport set to {name}"
            return await message.channel.send(name_message)

        if message.content.startswith(TravelList.AIRPORTDESTINATION):
            location = message.content[len(TravelList.AIRPORTDESTINATION) :]
            name, _ = session.travel_session.get_airport_by_location_name(location)
            name_message = f"Destination airport set to {name}"
            return await message.channel.send(name_message)

        if message.content.startswith(TravelList.FLIGHTDEPARTUREDATE):
            flight_departure_date = message.content[len(TravelList.FLIGHTDEPARTUREDATE) :]
            response_message = session.travel_session.add_to_querysting(
                "flightDepartureDate", flight_departure_date
            )
            return await message.channel.send(response_message)

        if message.content.startswith(TravelList.FLIGHTRETURNATDATE):
            flight_return_date = message.content[len(TravelList.FLIGHTRETURNATDATE) :]
            response_message = session.travel_session.add_to_querysting(
                "flightReturnDate", flight_return_date
            )
            return await message.channel.send(response_message)

        if message.content.startswith(TravelList.FLIGHTS):
            if session.travel_session:
                flights = session.travel_session.get_flight_data()
            else:
                flights = "no flight boilerplate"
            return await message.channel.send(flights)



        return await message.channel.send("Not valid command")

    async def on_reaction_add(self, reaction, user):
        session = self._get_session(reaction.message.channel.id)
        asking_for_guest = reaction.message.author

        if asking_for_guest == client.user:
            return

        if not session:
            return

        if session.user == user.id:
            if session.user == asking_for_guest.id:
                return await reaction.message.channel.send(f"Host user can't be guest!")

            session.add_guest(asking_for_guest.id)
            return await reaction.message.channel.send(
                f"{user} reacted with {reaction.emoji} and added {asking_for_guest} to this session"
            )

        return


client = MyClient()
client.run(DISCORD_KEY)
