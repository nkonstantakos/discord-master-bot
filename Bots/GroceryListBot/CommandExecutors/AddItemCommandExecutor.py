from Bots.GroceryListBot.Model.GroceryItem import GroceryItem
from CommandExecutor.CommandExecutor import CommandExecutor
from Utils import DateUtils


class AddItemCommandExecutor(CommandExecutor):

    def __init__(self, dao, command_map):
        """
        @type dao: GroceriesDao
        """
        self.dao = dao
        self.command_map = command_map

    def get_name(self):
        return "!add"

    def get_help_tip(self):
        return "Adds a new item to the current list"

    async def execute(self, client, command):
        grocery_item = GroceryItem(create_date=DateUtils.get_formatted_date(),
                                   item_name=command.command_params[0],
                                   item_owner=str(command.author.name),
                                   purchased=False,
                                   grocery_list_id=None,
                                   end_date=None,
                                   grocery_item_id=None)
        self.dao.add_grocery_item(grocery_item)
        await client.send_message(command.channel, "I added \"" + grocery_item.item_name + "\" to your list")
