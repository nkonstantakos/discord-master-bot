class Command(object):

    def __init__(self, message):
        """
        @type message: discord.Message
        """
        self.command_name = message.content.split(' ')[0]
        self.command_params = get_command_parameters(self.command_name, message.content)
        self.author = message.author
        self.channel = message.channel


def get_command_parameters(command_name, command_body):
    """
    @type command_name: str
    @type command_body: str
    """
    if len(command_name) == len(command_body):
        return []
    return command_body[len(command_name) + 1:].split(',')
