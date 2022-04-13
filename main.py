import os
from html import unescape

import discord
from dotenv import load_dotenv

from commands import HotelDetails, HotelList, HotelListDesc
from hotel_session import HotelSession

load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")


class MyClient(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.hotel_session = HotelSession()

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))

        if message.author == client.user:
            return

        if message.content.startswith(HotelList.HELP.value):
            commands = [c for c in zip(HotelList, HotelListDesc)]
            response_message = "Possible commands: \n"
            for command in commands:
                response_message += f"{command[0].value}{command[1].value} \n"
            await message.channel.send(response_message)

        if message.content.startswith(HotelList.CLEAR.value):
            self.hotel_session.querystring = None
            await message.channel.send("Filters cleaned")

        if message.content.startswith(HotelList.LOCATION.value):
            location = message.content[len(HotelList.LOCATION.value) :]
            name, _ = self.hotel_session.set_location_and_destination_id(location)
            name_message = f"Wybrano {name}"
            await message.channel.send(name_message)

        if message.content.startswith(HotelList.HOTELS.value):
            if self.hotel_session:
                hotels = self.hotel_session.get_hotels_for_destination_id()
            else:
                hotels = "no location boilerplate"
            await message.channel.send(hotels)

        if message.content.startswith(HotelList.ADULTS.value):
            adults = message.content[len(HotelList.ADULTS.value) :]
            response_message = self.hotel_session.add_to_querysting("adults1", adults)
            await message.channel.send(response_message)

        if message.content.startswith(HotelList.CHECK_IN.value):
            check_in = message.content[len(HotelList.CHECK_IN.value) :]
            response_message = self.hotel_session.add_to_querysting("checkIn", check_in)
            await message.channel.send(response_message)

        if message.content.startswith(HotelList.CHECK_OUT.value):
            check_out = message.content[len(HotelList.CHECK_OUT.value) :]
            response_message = self.hotel_session.add_to_querysting(
                "checkOut", check_out
            )
            await message.channel.send(response_message)

        if message.content.startswith(HotelList.CHILDREN.value):
            children = message.content[len(HotelList.CHILDREN.value) :]
            response_message = self.hotel_session.add_to_querysting(
                "children1", children
            )
            await message.channel.send(response_message)

        if message.content.startswith(HotelList.STAR_RATINGS.value):
            star_ratings = message.content[len(HotelList.STAR_RATINGS.value) :]
            response_message = self.hotel_session.add_to_querysting(
                "starRatings", star_ratings
            )
            await message.channel.send(response_message)

        if message.content.startswith(HotelList.PRICE_MIN.value):
            price_min = message.content[len(HotelList.PRICE_MIN.value) :]
            response_message = self.hotel_session.add_to_querysting(
                "priceMin", price_min
            )
            await message.channel.send(response_message)

        if message.content.startswith(HotelList.PRICE_MAX.value):
            price_max = message.content[len(HotelList.PRICE_MAX.value) :]
            response_message = self.hotel_session.add_to_querysting(
                "priceMax", price_max
            )
            await message.channel.send(response_message)

        # BEST_SELLER, STAR_RATING_HIGHEST_FIRST, STAR_RATING_LOWEST_FIRST, DISTANCE_FROM_LANDMARK, GUEST_RATING, PRICE_HIGHEST_FIRST, PRICE
        if message.content.startswith(HotelList.SORT_ORDER.value):
            sort = message.content[len(HotelList.SORT_ORDER.value) :]
            response_message = self.hotel_session.add_to_querysting("sortOrder", sort)
            await message.channel.send(response_message)

        if message.content.startswith(HotelList.GUEST_RATING_MINIMUM.value):
            guest_rating_minimum = message.content[
                len(HotelList.GUEST_RATING_MINIMUM.value) :
            ]
            response_message = self.hotel_session.add_to_querysting(
                "guestRatingMin", guest_rating_minimum
            )
            await message.channel.send(response_message)

        if message.content.startswith("$test"):

            response_message = unescape("total 155 € for 5&nbsp;nights")
            await message.channel.send(response_message)


client = MyClient()
client.run(DISCORD_KEY)
