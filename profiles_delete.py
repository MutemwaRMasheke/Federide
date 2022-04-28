#-----------------------------------------------------------------------
# profiles_delete.py
# Author: Mutemwa Masheke
# 
# Deletes a profile using name, federate, email, location, age, role 
# information
#-----------------------------------------------------------------------

from operator import contains
import os.path
from contextlib import closing
from sqlite3 import connect

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = 'federide.sqlite'

#-----------------------------------------------------------------------
def delete_profile(user_key):
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:
            sql_statement = "DELETE FROM profiles WHERE key LIKE ?"
            cursor.execute(sql_statement, [user_key])

#-----------------------------------------------------------------------

if __name__ == "__main__":
    delete_profile("12345")