from Bots.GroceryListBot.Model.GroceryItem import GroceryItem
from Command.Command import Command
from Utils import DateUtils


class AddGroceryItemCommand(Command):

    def get_name(self):
        return "!add"

    def __init__(self, dao):
        self.dao = dao

    async def execute(self, client, message):
        grocery_item = GroceryItem(create_date=DateUtils.get_formatted_date(),
                                   item_name=str(message.content)[5:],
                                   item_owner=str(message.author.name),
                                   grocery_list_id=None,
                                   end_date=None,
                                   grocery_item_id=None)
        self.dao.add_grocery_item(grocery_item)
        await client.send_message(message.channel, "I added " + grocery_item.item_name + " to your list")
