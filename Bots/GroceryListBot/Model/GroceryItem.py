class GroceryItem(object):
    def __init__(self,
                 grocery_item_id,
                 grocery_list_id,
                 item_name,
                 item_owner,
                 purchased,
                 create_date,
                 end_date):
        self.grocery_item_id = grocery_item_id
        self.grocery_list_id = grocery_list_id
        self.item_name = item_name
        self.item_owner = item_owner
        self.purchased = purchased
        self.create_date = create_date
        self.end_date = end_date
