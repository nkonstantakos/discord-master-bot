from CommandExecutor.CommandExecutor import CommandExecutor
from Bots.GroceryListBot.Dao.GroceriesDao import GroceriesDao


class ClearListCommandExecutor(CommandExecutor):

    def get_name(self):
        return "!clear"

    def get_help_tip(self):
        return "Starts a new grocery list"

    def __init__(self, dao, command_map):
        """
        @type dao: GroceriesDao
        """
        self.dao = dao
        self.command_map = command_map

    async def execute(self, client, command):
        if len(command.command_params) and command.command_params[0] == 'all':
            self.dao.start_new_list()
        else:
            self.dao.start_new_list_with_carryover()
        await client.send_message(command.channel, "I've cleared the list.")
