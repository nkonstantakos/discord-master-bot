import discord

from Bots.GroceryListBot.GroceryListBotController import GroceryListBotController
from Model.Command import Command

client = discord.Client()
controller = GroceryListBotController()


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

client.run('')
