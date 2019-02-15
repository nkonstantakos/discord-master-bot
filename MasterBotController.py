import discord

from Bots.GroceryListBot.GroceryListBotController import GroceryListBotController

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
        print('its me')
        return

    await controller.on_message(client, message)

client.run('')
