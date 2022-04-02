import os

from dotenv import load_dotenv

import discord
from commands import HotelDetails, HotelList
from place import get_hotels_for_location

client = discord.Client()

load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(HotelList.LOCATION):
        location = message.content[len(HotelList.LOCATION) :]
        response_message = get_hotels_for_location(location)
        await message.channel.send(response_message)

    if message.content.startswith(HotelList.ADULTS):
        location = message.content[len(HotelList.ADULTS) :]
        response_message = get_hotels_for_location(location)
        await message.channel.send(response_message)


client.run(DISCORD_KEY)
