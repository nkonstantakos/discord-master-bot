def create_grocery_list_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS GROCERY_LIST
                     (grocery_list_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     create_date TEXT,
                     end_date TEXT)''')


def add_first_list(conn, current_date):
    conn.execute('''INSERT INTO GROCERY_LIST(create_date, end_date)
                    SELECT ?, ?
                    WHERE NOT EXISTS (SELECT * FROM GROCERY_LIST)''', (current_date, None))


def start_new_list(conn, current_date):
    conn.execute('''UPDATE GROCERY_LIST
                    SET end_date =  ?
                    WHERE grocery_list_id = (SELECT MAX(grocery_list_id) FROM GROCERY_LIST)''', (current_date,))
    conn.commit()
    conn.execute('''INSERT INTO GROCERY_LIST(create_date, end_date)
                    SELECT ?, ?''', (current_date, None))
    conn.commit()
