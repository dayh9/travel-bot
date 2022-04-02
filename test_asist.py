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

    if message.content.startswith(HotelList.CHECKIN):
        check_in = message.content[len(HotelList.CHECKIN) :]
        response_message = get_hotels_for_location(check_in)
        await message.channel.send(response_message)

    if message.content.startswith(HotelList.CHECKOUT):
        check_out = message.content[len(HotelList.CHECKOUT) :]
        response_message = get_hotels_for_location(check_out)
        await message.channel.send(response_message)

    if message.content.startswith(HotelList.ADULTS1):
        adults_1 = message.content[len(HotelList.ADULTS1) :]
        response_message = get_hotels_for_location(adults_1)
        await message.channel.send(response_message)

    if message.content.startswith(HotelList.CHILDREN1):
        children_1 = message.content[len(HotelList.CHILDREN1) :]
        response_message = get_hotels_for_location(children_1)
        await message.channel.send(response_message)

    if message.content.startswith(HotelList.STARRATINGS):
        star_ratings = message.content[len(HotelList.STARRATINGS) :]
        response_message = get_hotels_for_location(star_ratings)
        await message.channel.send(response_message)

    if message.content.startswith(HotelList.PRICEMIN):
        price_min = message.content[len(HotelList.PRICEMIN) :]
        response_message = get_hotels_for_location(price_min)
        await message.channel.send(response_message)

    if message.content.startswith(HotelList.PRICEMAX):
        price_max = message.content[len(HotelList.PRICEMAX) :]
        response_message = get_hotels_for_location(price_max)
        await message.channel.send(response_message)

    # BEST_SELLER, STAR_RATING_HIGHEST_FIRST, STAR_RATING_LOWEST_FIRST, DISTANCE_FROM_LANDMARK, GUEST_RATING, PRICE_HIGHEST_FIRST, PRICE
    if message.content.startswith(HotelList.SORTORDER):
        sort = message.content[len(HotelList.SORTORDER) :]
        response_message = get_hotels_for_location(sort)
        await message.channel.send(response_message)

    if message.content.startswith(HotelList.GUESTRATINGMINIMUM):
        guest_rating_minimum = message.content[len(HotelList.GUESTRATINGMINIMUM) :]
        response_message = get_hotels_for_location(guest_rating_minimum)
        await message.channel.send(response_message)

client.run(DISCORD_KEY)
