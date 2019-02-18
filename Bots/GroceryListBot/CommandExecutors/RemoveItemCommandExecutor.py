from CommandExecutor.CommandExecutor import CommandExecutor
from Bots.GroceryListBot.Dao.GroceriesDao import GroceriesDao


class RemoveItemCommandExecutor(CommandExecutor):

    def get_name(self):
        return "!remove"

    def __init__(self, dao):
        """
        @type dao: GroceriesDao
        """
        self.dao = dao

    async def execute(self, client, command):
        item_number = int(command.command_params[0])
        self.dao.remove_grocery_item(item_number)
        await client.send_message(command.channel, "I removed item #" + str(item_number) + " from your list")
