class GroceryList(object):
    def __init__(self,
                 grocery_list_id,
                 create_date,
                 end_date):
        self.grocery_list_id = grocery_list_id
        self.create_date = create_date
        self.end_date = end_date


def create_grocery_list_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS GROCERY_LIST
                     (grocery_list_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     create_date TEXT,
                     end_date TEXT)''')

