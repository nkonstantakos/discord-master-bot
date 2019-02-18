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
    """
    @type grocery_item: GroceryItem
    """
    conn.execute('INSERT INTO GROCERY_ITEM (grocery_list_id, item_name, item_owner, create_date)'
                 'VALUES ((SELECT MAX(grocery_list_id) FROM GROCERY_LIST), ?, ?, ?)',
                 (grocery_item.item_name,
                  grocery_item.item_owner,
                  grocery_item.create_date))


def get_latest_list(conn):
    c = conn.cursor()
    c.execute('''SELECT *
                 FROM GROCERY_ITEM
                 WHERE grocery_list_id = (SELECT MAX(grocery_list_id) FROM GROCERY_LIST)''')
    result = c.fetchall()
    items = []
    for row in result:
        items.append(GroceryItem(row[0], row[1], row[2], row[3], row[4], row[5]))
    return items


def remove_item_from_list(conn, item_number):
    """
    @type item_number: int
    """
    conn.execute('''DELETE FROM GROCERY_ITEM
                    WHERE grocery_item_id = ?''', (item_number,))
