import discord
from Bots.GroceryListBot.CommandExecutors.HelpGroceriesCommandExecutor import HelpGroceriesCommandExecutor
from Bots.GroceryListBot.CommandExecutors.PrintListCommandExecutor import PrintListCommandExecutor
from Bots.GroceryListBot.CommandExecutors.ClearListCommandExecutor import ClearListCommandExecutor
from Bots.GroceryListBot.CommandExecutors.RemoveItemCommandExecutor import RemoveItemCommandExecutor
from Bots.GroceryListBot.CommandExecutors.AddItemCommandExecutor import AddItemCommandExecutor
from Bots.GroceryListBot.Dao.GroceriesDao import GroceriesDao
from Model.Command import Command
from Controller.Controller import Controller


class GroceryListBotController(Controller):

    def __init__(self):
        self.dao = GroceriesDao('Bots/GroceryListBot/groceries.db')
        self.dao.create_tables()
        self.dao.start_first_list()
        add_command = AddItemCommandExecutor(self.dao)
        help_command = HelpGroceriesCommandExecutor(self.dao)
        print_command = PrintListCommandExecutor(self.dao)
        clear_command = ClearListCommandExecutor(self.dao)
        remove_command = RemoveItemCommandExecutor(self.dao)
        self.command_map = dict([(add_command.get_name(), add_command),
                                 (help_command.get_name(), help_command),
                                 (print_command.get_name(), print_command),
                                 (clear_command.get_name(), clear_command),
                                 (remove_command.get_name(), remove_command)])

    async def on_message(self, client, command):
        """
        @type client: discord.Client
        @type command: Command
        """

        if str(command.author) == "GroceryListBot#5417":
            return

        if command.command_name in self.command_map:
            await self.command_map[command.command_name].execute(client, command)
        else:
            await client.send_message(command.channel, "Sorry I don't support that command yet :frowning:")
