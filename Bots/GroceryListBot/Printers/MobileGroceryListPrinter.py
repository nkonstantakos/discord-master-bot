from Bots.GroceryListBot.Model.GroceryItem import GroceryItem
from Bots.GroceryListBot.Printers.GroceryListPrinter import GroceryListPrinter


class MobileGroceryListPrinter(GroceryListPrinter):

    @staticmethod
    def print_list(items):
        """
        @type items: list[GroceryItem]
        """
        response = ""
        for item in items:
            response += format_row(item)
        return response


def format_row(item):
    row = str(item.grocery_item_id) + ". " + item.item_name + "\n"
    if item.purchased:
        row = "~~" + row + "~~"
    return row

