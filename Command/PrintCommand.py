from Command.Command import Command


class PrintCommand(Command):

    def get_name(self):
        return "!print"

    async def execute(self, client, message):
        raise NotImplementedError("Action not yet implemented")
