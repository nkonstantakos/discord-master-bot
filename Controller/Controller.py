from Model.Command import Command


class Controller(object):

    async def on_message(self, client, command):
        """
        @type client: discord.Client
        @type command: Command
        """
        raise NotImplementedError("No implementation of on_message defined")
