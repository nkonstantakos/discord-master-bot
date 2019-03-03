import asyncio

import discord
import configparser
import time
from aiohttp import ClientOSError
from Bots.GroceryListBot.GroceryListBotController import GroceryListBotController
from Model.Command import Command


def run():
    controller = GroceryListBotController()
    config = configparser.ConfigParser()
    config.read('properties.ini')
    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user)
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        """
        @type message: discord.Message
        """

        if str(message.author) == client.user:
            return
        elif message.content.startswith("!"):
            command = Command(message)
            await controller.on_message(client, command)

    loop = asyncio.get_event_loop()
    while True:
        try:
            loop.run_until_complete(client.start(config['DISCORD']['botKey']))
        except ClientOSError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            msg = template.format(type(ex).__name__, ex.args)
            print(msg)
        time.sleep(int(config['DISCORD']['reconnect_delay']))

run()
