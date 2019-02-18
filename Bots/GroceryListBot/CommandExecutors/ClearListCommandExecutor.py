from CommandExecutor.CommandExecutor import CommandExecutor
from Bots.GroceryListBot.Dao.GroceriesDao import GroceriesDao


class ClearListCommandExecutor(CommandExecutor):

    def get_name(self):
        return "!clear"

    def __init__(self, dao):
        """
        @type dao: GroceriesDao
        """
        self.dao = dao

    async def execute(self, client, command):
        self.dao.start_new_list()
        await client.send_message(command.channel, "I've cleared the list.")
