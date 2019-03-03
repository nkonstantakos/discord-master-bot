import datetime
import sqlite3

from Bots.GroceryListBot.Dao.Tables import GroceryListDao
from Bots.GroceryListBot.Dao.Tables import GroceryItemDao


class GroceriesDao(object):

    def __init__(self, db_name):
        self.db_name = db_name

    def create_tables(self):
        conn = self.get_db_connection()
        GroceryListDao.create_grocery_list_table(conn)
        GroceryItemDao.create_grocery_item_table(conn)
        commit_and_close(conn)

    def start_first_list(self):
        conn = self.get_db_connection()
        GroceryListDao.add_first_list(conn, get_formatted_date())
        commit_and_close(conn)

    def add_grocery_item(self, grocery_item):
        conn = self.get_db_connection()
        GroceryItemDao.insert_grocery_item_record(conn, grocery_item)
        commit_and_close(conn)

    def got_grocery_items(self, item_ids):
        conn = self.get_db_connection()
        GroceryItemDao.got_grocery_items(conn, item_ids)
        commit_and_close(conn)

    def get_grocery_items(self):
        conn = self.get_db_connection()
        items = GroceryItemDao.get_latest_list(conn)
        commit_and_close(conn)
        return items

    def start_new_list(self):
        conn = self.get_db_connection()
        GroceryListDao.start_new_list(conn, get_formatted_date())
        commit_and_close(conn)

    def start_new_list_with_carryover(self):
        conn = self.get_db_connection()
        GroceryListDao.start_new_list(conn, get_formatted_date())
        GroceryItemDao.carryover_items(conn)
        commit_and_close(conn)

    def get_db_connection(self):
        return sqlite3.connect(self.db_name)

    def remove_grocery_item(self, item_number):
        conn = self.get_db_connection()
        GroceryItemDao.remove_item_from_list(conn, item_number)
        commit_and_close(conn)


def commit_and_close(conn):
    conn.commit()
    conn.close()


def get_formatted_date():
    date = datetime.datetime.now()
    return date.strftime('%Y-%m-%d %H:%M:%S')
