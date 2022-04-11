#-----------------------------------------------------------------------
# profiles_query.py
# Author: Mutemwa Masheke 
#-----------------------------------------------------------------------

from operator import contains
import os.path
from contextlib import closing
from sqlite3 import connect, Row

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = 'federide.sqlite'

#-----------------------------------------------------------------------
def retrieve_federate(user_key, federate_name):
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    with connect(DATABASE_URL, uri=True) as connection:
        connection.row_factory = Row
        with closing(connection.cursor()) as cursor:
            sql_statement = 'SELECT name, federate, email, location, age, role FROM profiles '
            sql_statement += "WHERE federate LIKE ? "
            cursor.execute(sql_statement, [federate_name])
            row_list = [dict(row) for row in cursor.fetchall()]

            if not row_list:
                raise Exception("Federate doesn't exist")

            return row_list

#-----------------------------------------------------------------------

if __name__ == "__main__":
    print(retrieve_federate("12345", "The Driver's Coop"))