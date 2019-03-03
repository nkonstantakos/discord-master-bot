import prettytable
from Bots.GroceryListBot.Printers.GroceryListPrinter import GroceryListPrinter


class DesktopGroceryListPrinter(GroceryListPrinter):

    @staticmethod
    def print_list(items):
        """
        @type items: GroceryItem[]
        """
        response = prettytable.PrettyTable(["ID", "Name", "Added By", "Purchased"])
        for item in items:
            response.add_row([item.grocery_item_id, item.item_name, item.item_owner, item.purchased])
        return "``" + response.get_string() + "``"

