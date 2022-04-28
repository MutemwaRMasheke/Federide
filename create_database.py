#-----------------------------------------------------------------------
# create_database.py
# Author: Mutemwa Masheke 
#
# This program creates a SQLite database file to be used to store the 
# user profile information of the federation
#-----------------------------------------------------------------------

import sqlite3, os
from contextlib import closing
from sqlite3 import connect

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = "federide.sqlite"

#-----------------------------------------------------------------------

# creates a database file called "federide.sqlite" 
def create_db():

    # no duplicate database files
    if os.path.isfile(DB_FILENAME):
        raise Exception('file already exists')

    # create a sqlite file
    connection = sqlite3.connect(DB_FILENAME)
    connection.commit()
    connection.close()

#-----------------------------------------------------------------------

# creates a table of profiles in the database federide.sqlite
def create_profiles():
    table_name = "profiles"

    # ensure database file exists in the directory
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    # create a profiles table
    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                (name TEXT, email TEXT, federate TEXT, location TEXT, key TEXT, age INT, role TEXT)''')

#-----------------------------------------------------------------------

if __name__ == "__main__":
    create_db()
    create_profiles()