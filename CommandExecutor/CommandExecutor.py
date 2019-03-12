from Model.Command import Command


class CommandExecutor(object):

    def get_name(self):
        raise NotImplementedError("Name not yet set")

    def get_help_tip(self):
        return ""

    async def execute(self, client, command):
        """
        @type client: discord.Client
        @type command: Command
        """
        raise NotImplementedError("Action not yet implemented")

    def get_name_length(self):
        return self.get_name().length

