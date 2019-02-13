import sqlite3

from GroceryListDao.Tables import GroceryList

from GroceryListBot.GroceryListDao.Tables import GroceryItem


class GroceryListDao(object):

    def __init__(self, db_name):
        self.db_name = db_name

    def create_tables(self):
        conn = self.get_db_connection()
        GroceryList.create_grocery_list_table(conn)
        GroceryItem.create_grocery_item_table(conn)
        commit_and_close(conn)

    def get_db_connection(self):
        return sqlite3.connect(self.db_name)


def commit_and_close(conn):
    conn.commit()
    conn.close()

