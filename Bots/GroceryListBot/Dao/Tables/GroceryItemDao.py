from Bots.GroceryListBot.Model.GroceryItem import GroceryItem


def create_grocery_item_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS GROCERY_ITEM
                     (grocery_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     grocery_list_id INTEGER,
                     item_name TEXT,
                     item_owner TEXT,
                     create_date TEXT,
                     end_date TEXT,
                     FOREIGN KEY(grocery_list_id) REFERENCES GROCERY_LIST (grocery_list_id))''')


def insert_grocery_item_record(conn, grocery_item):
    conn.execute('INSERT INTO GROCERY_ITEM (grocery_list_id, item_name, item_owner, create_date)'
                 'VALUES (?, ?, ?, ?)',
                 (1,
                  grocery_item.item_name,
                  grocery_item.item_owner,
                  grocery_item.create_date))


def get_items_in_list(conn, grocery_list_id):
    c = conn.cursor()
    c.execute("SELECT * FROM GROCERY_ITEM WHERE grocery_list_id = 1")
    result = c.fetchall()
    items = []
    for row in result:
        items.append(GroceryItem(row[0], row[1], row[2], row[3], row[4], row[5]))
    return items
