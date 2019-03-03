from CommandExecutor.CommandExecutor import CommandExecutor


class GotItemCommandExecutor(CommandExecutor):

    def get_name(self):
        return "!got"

    def __init__(self, dao):
        self.dao = dao

    async def execute(self, client, command):
        self.dao.got_grocery_items(command.command_params)
        await client.send_message(command.channel, "I marked those as purchased.")
