from CommandExecutor.CommandExecutor import CommandExecutor


class HelpCommandExecutor(CommandExecutor):

    def get_name(self):
        return "!help"

    async def execute(self, client, command):
        raise NotImplementedError("Action not yet implemented")
