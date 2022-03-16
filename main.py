import os

import discord
from dotenv import load_dotenv

from place import get_place
from travel import get_sth

load_dotenv()

DISCORD_KEY = os.getenv("DISCORD_KEY")


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))

        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")

        if message.content.startswith("elo"):
            await message.channel.send("no elo")

        if message.content.startswith("daj"):
            sth = get_place()
            sth = "dalo"
            await message.channel.send(sth)

        if message.content.startswith("kuba"):
            sth = get_sth()
            sth = "dalo kuba"
            await message.channel.send(sth)


client = MyClient()
client.run(DISCORD_KEY)
