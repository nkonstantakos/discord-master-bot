from CommandExecutor.CommandExecutor import CommandExecutor


class PrintCommandExecutor(CommandExecutor):

    def get_name(self):
        return "!print"

    async def execute(self, client, command):
        raise NotImplementedError("Action not yet implemented")
