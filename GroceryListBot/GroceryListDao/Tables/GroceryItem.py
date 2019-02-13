class GroceryItem(object):
    def __init__(self,
                 grocery_item_id,
                 grocery_list_id,
                 item_name,
                 item_owner,
                 create_date,
                 end_date):
        self.grocery_item_id = grocery_item_id
        self.grocery_list_id = grocery_list_id
        self.item_name = item_name
        self.item_owner = item_owner
        self.create_date = create_date
        self.end_date = end_date


def create_grocery_item_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS GROCERY_ITEM
                     (grocery_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     grocery_list_id INTEGER,
                     item_name TEXT,
                     item_owner TEXT,
                     create_date TEXT,
                     end_date TEXT,
                     FOREIGN KEY(grocery_list_id) REFERENCES GROCERY_LIST (grocery_list_id))''')


def insert_grocery_item_record(conn, groceryItem):
    conn.execute('INSERT INTO GROCERY_ITEM (grocery_list_id, item_name, item_owner, create_date, end_date)'
                 'VALUES (?, ?, ?, ?, ?)',
                 (groceryItem.grocery_list_id,
                  groceryItem.item_name,
                  groceryItem.item_owner,
                  groceryItem.create_date,
                  groceryItem.end_date))
