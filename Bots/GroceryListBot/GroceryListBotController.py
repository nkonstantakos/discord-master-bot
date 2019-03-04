import discord
from Bots.GroceryListBot.CommandExecutors.HelpGroceriesCommandExecutor import HelpGroceriesCommandExecutor
from Bots.GroceryListBot.CommandExecutors.PrintListCommandExecutor import PrintListCommandExecutor
from Bots.GroceryListBot.CommandExecutors.ClearListCommandExecutor import ClearListCommandExecutor
from Bots.GroceryListBot.CommandExecutors.RemoveItemCommandExecutor import RemoveItemCommandExecutor
from Bots.GroceryListBot.CommandExecutors.AddItemCommandExecutor import AddItemCommandExecutor
from Bots.GroceryListBot.CommandExecutors.GotItemCommandExecutor import GotItemCommandExecutor
from Bots.GroceryListBot.Dao.GroceriesDao import GroceriesDao
from Model.Command import Command
from Controller.Controller import Controller


class GroceryListBotController(Controller):

    def __init__(self):
        self.dao = GroceriesDao('Bots/GroceryListBot/groceries.db')
        self.dao.create_tables()
        self.dao.start_first_list()
        self.command_map = dict()
        self.initialize_command_map(self.initialize_command_executors())

    def initialize_command_map(self, command_list):
        for command in command_list:
            self.command_map[command.get_name()] = command

    def initialize_command_executors(self):
        command_list = [AddItemCommandExecutor(self.dao),
                        AddItemCommandExecutor(self.dao),
                        HelpGroceriesCommandExecutor(self.dao),
                        PrintListCommandExecutor(self.dao),
                        RemoveItemCommandExecutor(self.dao),
                        GotItemCommandExecutor(self.dao)]
        return command_list

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
