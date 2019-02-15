from Bots.GroceryListBot.Model.GroceryItem import GroceryItem
from Command.Command import Command
from Bots.GroceryListBot.Dao.GroceriesDao import GroceriesDao
from Utils import DateUtils


class AddGroceryItemCommand(Command):

    def get_name(self):
        return "!remove"

    def __init__(self, dao):
        """
        @type dao: GroceriesDao
        """
        self.dao = dao

    async def execute(self, client, message):
        message_body = str(message.content)[5:]
        item_number = int(message_body.split(" ")[0])
        self.dao.remove_grocery_item(item_number)
        await client.send_message(message.channel, "I removed item #" + str(item_number) + " from your list")
