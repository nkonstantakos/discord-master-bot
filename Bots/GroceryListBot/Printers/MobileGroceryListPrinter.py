from Bots.GroceryListBot.Model.GroceryItem import GroceryItem
from Bots.GroceryListBot.Printers.GroceryListPrinter import GroceryListPrinter


class MobileGroceryListPrinter(GroceryListPrinter):

    @staticmethod
    def print_list(items):
        """
        @type items: list[GroceryItem]
        """
        response = ""
        iterator = 1
        for item in items:
            response += str(item.grocery_item_id) + ". " + item.item_name + "\n"
            iterator += 1
        return response
