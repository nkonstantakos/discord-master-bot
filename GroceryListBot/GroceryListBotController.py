import discord
from GroceryListDao.GroceryListDao import GroceryListDao

from GroceryListBot.GroceryListDao.Tables.GroceryItem import GroceryItem


async def on_message(client, message):
    """
    @type client: discord.Client
    @type message: discord.Message
    """

    if str(message.author) == "GroceryListBot#5417":
        return

    dao = GroceryListDao('groceries.db')
    dao.create_tables()
    if message.content.startswith('!help'):
        response =  "```!help:     Prints available commands\n"
        response += "!print:    Prints the contents of the current list\n"
        response += "!add:      Adds a new item to the current list\n"
        response += "!remove:   Removes a given item from the current list\n"
        response += "!clear:    Starts a new grocery list\n```"
        await client.send_message(message.channel, response)
    elif message.content.startswith('!temp'):
        groceryItem = GroceryItem(grocery_list_id=1, create_date='asdas')
        await client.send_message(message.channel, 'I added your item')


def append_message(original, new):
    """
    @type original: basestring
    @type new: basestring
    """
    return original + "\n" + new
