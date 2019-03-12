from CommandExecutor.HelpCommandExecutor import HelpCommandExecutor

HELP_TEMPLATE = "{0}: {1}\n"
RESPONSE_TEMPLATE = "```{0}```"


class HelpGroceriesCommandExecutor(HelpCommandExecutor):

    def __init__(self, dao, command_map):
        """
        @type dao: GroceriesDao
        @type command_map: dict
        """
        self.dao = dao
        self.command_map = command_map

    async def execute(self, client, command):
        response = ""
        for command_executor in self.command_map.values():
            if command_executor.get_help_tip():
                response += add_tip(command_executor)
        response = RESPONSE_TEMPLATE.format(response)
        await client.send_message(command.channel, response)


def add_tip(command_executor):
    return HELP_TEMPLATE.format(command_executor.get_name(), command_executor.get_help_tip())
