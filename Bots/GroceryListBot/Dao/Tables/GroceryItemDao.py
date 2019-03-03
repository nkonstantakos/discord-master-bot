from Bots.GroceryListBot.Model.GroceryItem import GroceryItem


def create_grocery_item_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS GROCERY_ITEM
                     (grocery_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     grocery_list_id INTEGER,
                     item_name TEXT,
                     item_owner TEXT,
                     purchased INTEGER,
                     create_date TEXT,
                     end_date TEXT,
                     FOREIGN KEY(grocery_list_id) REFERENCES GROCERY_LIST (grocery_list_id))''')


def insert_grocery_item_record(conn, grocery_item):
    """
    @type grocery_item: GroceryItem
    """
    conn.execute('INSERT INTO GROCERY_ITEM (grocery_list_id, item_name, item_owner, purchased, create_date)'
                 'VALUES ((SELECT MAX(grocery_list_id) FROM GROCERY_LIST), ?, ?, ?, ?)',
                 (grocery_item.item_name,
                  grocery_item.item_owner,
                  int(grocery_item.purchased),
                  grocery_item.create_date))


def got_grocery_items(conn, item_ids):
    """
    @type item_ids: int[]
    """
    conn.execute('''UPDATE GROCERY_ITEM
                    SET purchased = 1
                    WHERE grocery_item_id IN ({sequence})'''.format(sequence=','.join(['?']*len(item_ids))), item_ids)
    conn.commit()


def get_latest_list(conn):
    c = conn.cursor()
    c.execute('''SELECT *
                 FROM GROCERY_ITEM
                 WHERE grocery_list_id = (SELECT MAX(grocery_list_id) FROM GROCERY_LIST)''')
    result = c.fetchall()
    items = []
    for row in result:
        items.append(GroceryItem(row[0], row[1], row[2], row[3], bool(row[4]), row[5], row[6]))
    return items


def remove_item_from_list(conn, item_number):
    """
    @type item_number: int
    """
    conn.execute('''DELETE FROM GROCERY_ITEM
                    WHERE grocery_item_id = ?''', (item_number,))


def carryover_items(conn):
    conn.execute('''UPDATE GROCERY_ITEM
                    SET grocery_list_id =  (SELECT MAX(grocery_list_id) FROM GROCERY_LIST)
                    WHERE purchased = 0
                    AND grocery_list_id = (SELECT MAX(grocery_list_id)
                                            FROM GROCERY_LIST
                                            WHERE grocery_list_id NOT IN (SELECT MAX(grocery_list_id)
                                                                          FROM GROCERY_LIST))''', )
    conn.commit()
