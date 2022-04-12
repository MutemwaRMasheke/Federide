import sqlite3, os
from contextlib import closing
from sqlite3 import connect

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = "federide.sqlite"

def create_db():
    if os.path.isfile(DB_FILENAME):
        raise Exception('file already exists')

    connection = sqlite3.connect(DB_FILENAME)
    connection.commit()
    connection.close()

def create_table(table_name):
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                (name TEXT, email TEXT, federate TEXT, location TEXT, key TEXT, age INT, role TEXT)''')

if __name__ == "__main__":
    create_db()
    create_table("profiles")