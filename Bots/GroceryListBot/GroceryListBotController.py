import discord
from Bots.GroceryListBot.Commands.HelpGroceryListCommand import HelpGroceryListCommand
from Bots.GroceryListBot.Commands.PrintGroceryListCommand import PrintGroceryListCommand
from Bots.GroceryListBot.Dao.GroceriesDao import GroceriesDao

from Bots.GroceryListBot.Commands.AddGroceryItemCommand import AddGroceryItemCommand
from Controller.Controller import Controller


class GroceryListBotController(Controller):

    def __init__(self):
        self.dao = GroceriesDao('Bots/GroceryListBot/groceries.db')
        self.dao.create_tables()
        self.dao.start_first_list()
        add_command = AddGroceryItemCommand(self.dao)
        help_command = HelpGroceryListCommand(self.dao)
        print_command = PrintGroceryListCommand(self.dao)
        self.command_map = dict([(add_command.get_name(), add_command),
                                 (help_command.get_name(), help_command),
                                 (print_command.get_name(), print_command)])

    async def on_message(self, client, message):
        """
        @type client: discord.Client
        @type message: discord.Message
        """

        if str(message.author) == "GroceryListBot#5417":
            return

        command = self.command_map[message.content.split(' ')[0]]
        if command is not None:
            await command.execute(client, message)
        else:
            await client.send_message(message.channel, "Sorry I don't support that command yet :frowning:")
