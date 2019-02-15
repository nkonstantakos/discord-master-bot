from Command.Command import Command


class HelpCommand(Command):

    def get_name(self):
        return "!help"

    async def execute(self, client, message):
        raise NotImplementedError("Action not yet implemented")
