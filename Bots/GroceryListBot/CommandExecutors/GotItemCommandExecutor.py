from CommandExecutor.CommandExecutor import CommandExecutor


class GotItemCommandExecutor(CommandExecutor):

    def get_name(self):
        return "!got"

    def get_help_tip(self):
        return "Marks the item(s) as purchased"

    def __init__(self, dao, command_map):
        """
        @type dao: GroceriesDao
        """
        self.dao = dao
        self.command_map = command_map

    async def execute(self, client, command):
        self.dao.got_grocery_items(command.command_params)
        await client.send_message(command.channel, "I marked those as purchased.")
