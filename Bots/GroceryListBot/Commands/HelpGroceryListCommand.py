from Command.HelpCommand import HelpCommand


class HelpGroceryListCommand(HelpCommand):

    def __init__(self, dao):
        self.dao = dao

    async def execute(self, client, message):
        response = "```!help:     Prints available commands\n"
        response += "!print:    Prints the contents of the current list\n"
        response += "!add:      Adds a new item to the current list\n"
        response += "!remove:   Removes a given item from the current list\n"
        response += "!clear:    Starts a new grocery list\n```"
        await client.send_message(message.channel, response)
