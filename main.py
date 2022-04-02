import os

from dotenv import load_dotenv

import discord
from commands import HotelDetails, HotelList
from hotel_session import HotelSession
from place import get_hotels_for_location

load_dotenv()

DISCORD_KEY = os.getenv("DISCORD_KEY")


class MyClient(discord.Client):
    def __init__(self, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.hotel_session = None

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))

        if message.author == client.user:
            return

        if message.content.startswith(HotelList.LOCATION.value):
            location = message.content[len(HotelList.LOCATION.value) :]
            self.hotel_session = HotelSession(location)
            name, _ = self.hotel_session.get_name_and_destination_id()
            await message.channel.send(name)

        if message.content.startswith(HotelList.HOTELS.value):
            # location = message.content[len(HotelList.HOTELS) :]
            hotels = self.hotel_session.get_hotels_for_destination_id()
            await message.channel.send(hotels)

        if message.content.startswith(HotelList.ADULTS.value):
            adults = message.content[len(HotelList.ADULTS.value) :]
            response = self.hotel_session.add_to_querysting("adults1", adults)
            await message.channel.send(response)


client = MyClient()
client.run(DISCORD_KEY)
