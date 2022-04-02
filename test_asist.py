import os

from dotenv import load_dotenv

import discord
from commands import HotelDetails, HotelList
from hotel_session import HotelSession
from place import get_hotels_for_location

client = discord.Client()

load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(HotelList.LOCATION.value):
        location = message.content[len(HotelList.LOCATION.value) :]
        hotel_session = HotelSession(location)
        name, _ = hotel_session.get_name_and_destination_id()
        await message.channel.send(name)

    if message.content.startswith(HotelList.HOTELS.value):
        # location = message.content[len(HotelList.HOTELS) :]
        hotels = hotel_session.get_hotels_for_destination_id()
        await message.channel.send(hotels)

    if message.content.startswith(HotelList.ADULTS.value):
        adults = message.content[len(HotelList.ADULTS.value) :]
        response = hotel_session.add_to_querysting("adults1", adults)
        await message.channel.send(response)

    # if message.content.startswith(HotelList.CHECK_IN):
    #     check_in = message.content[len(HotelList.CHECK_IN) :]
    #     response_message = get_hotels_for_location(check_in)
    #     await message.channel.send(response_message)

    # if message.content.startswith(HotelList.CHECK_OUT):
    #     check_out = message.content[len(HotelList.CHECK_OUT) :]
    #     response_message = get_hotels_for_location(check_out)
    #     await message.channel.send(response_message)

    # if message.content.startswith(HotelList.ADULTS):
    #     adults = message.content[len(HotelList.ADULTS) :]
    #     response_message = get_hotels_for_location(adults)
    #     await message.channel.send(response_message)

    # if message.content.startswith(HotelList.CHILDREN):
    #     children = message.content[len(HotelList.CHILDREN) :]
    #     response_message = get_hotels_for_location(children)
    #     await message.channel.send(response_message)

    # if message.content.startswith(HotelList.STAR_RATINGS):
    #     star_ratings = message.content[len(HotelList.STAR_RATINGS) :]
    #     response_message = get_hotels_for_location(star_ratings)
    #     await message.channel.send(response_message)

    # if message.content.startswith(HotelList.PRICE_MIN):
    #     price_min = message.content[len(HotelList.PRICE_MIN) :]
    #     response_message = get_hotels_for_location(price_min)
    #     await message.channel.send(response_message)

    # if message.content.startswith(HotelList.PRICE_MAX):
    #     price_max = message.content[len(HotelList.PRICE_MAX) :]
    #     response_message = get_hotels_for_location(price_max)
    #     await message.channel.send(response_message)

    # # BEST_SELLER, STAR_RATING_HIGHEST_FIRST, STAR_RATING_LOWEST_FIRST, DISTANCE_FROM_LANDMARK, GUEST_RATING, PRICE_HIGHEST_FIRST, PRICE
    # if message.content.startswith(HotelList.SORT_ORDER):
    #     sort = message.content[len(HotelList.SORT_ORDER) :]
    #     response_message = get_hotels_for_location(sort)
    #     await message.channel.send(response_message)

    # if message.content.startswith(HotelList.GUEST_RATING_MINIMUM):
    #     guest_rating_minimum = message.content[len(HotelList.GUEST_RATING_MINIMUM) :]
    #     response_message = get_hotels_for_location(guest_rating_minimum)
    #     await message.channel.send(response_message)


client.run(DISCORD_KEY)
