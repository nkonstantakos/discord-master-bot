import prettytable

from Command.PrintCommand import PrintCommand


class PrintGroceryListCommand(PrintCommand):

    def __init__(self, dao):
        self.dao = dao

    async def execute(self, client, message):
        items = self.dao.get_grocery_items(1) # type GroceryItem[]
        """
        @type items: GroceryItem[]
        """
        response = prettytable.PrettyTable(["ID", "Name", "Added By"])
        for item in items:
            response.add_row([item.grocery_item_id, item.item_name, item.item_owner])
        await client.send_message(message.channel, "``" + response.get_string() + "``")
