import os

from dotenv import load_dotenv

import discord
from place import get_hotels_for_location

client = discord.Client()

load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$location"):
        location = message.content[9:]
        response_message = get_hotels_for_location(location)
        await message.channel.send(response_message)


client.run(DISCORD_KEY)
