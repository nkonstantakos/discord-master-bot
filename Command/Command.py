class Command(object):

    def get_name(self):
        raise NotImplementedError("Name not yet set")

    async def execute(self, client, message):
        """
        @type client: discord.Client
        @type message: discord.Message
        """
        raise NotImplementedError("Action not yet implemented")

    def get_name_length(self):
        return self.get_name().length

