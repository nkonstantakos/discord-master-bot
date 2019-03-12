from CommandExecutor.PrintCommandExecutor import PrintCommandExecutor
from Bots.GroceryListBot.Printers.DesktopGroceryListPrinter import DesktopGroceryListPrinter
from Bots.GroceryListBot.Printers.MobileGroceryListPrinter import MobileGroceryListPrinter


class PrintListCommandExecutor(PrintCommandExecutor):

    def get_help_tip(self):
        return "Prints the grocery list params: [mobile]"

    def __init__(self, dao, command_map):
        """
        @type dao: GroceriesDao
        @type command_map: dict
        """
        self.dao = dao
        self.command_map = command_map

    async def execute(self, client, command):
        items = self.dao.get_grocery_items()
        """
        @type items: GroceryItem[]
        """
        response = ""
        if not command.command_params or command.command_params[0] == "desktop":
            response = DesktopGroceryListPrinter.print_list(items)
        elif command.command_params[0] == "mobile":
            response = MobileGroceryListPrinter.print_list(items)

        await client.send_message(command.channel, "" + response + "")
