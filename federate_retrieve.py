#-----------------------------------------------------------------------
# federate_retreive.py
# Author: Mutemwa Masheke
# 
# Returns all worker's names in a federate from the profile database
#-----------------------------------------------------------------------

import os.path
from contextlib import closing
from sqlite3 import connect, Row

from profiles_get import get_profiles

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = 'federide.sqlite'

#-----------------------------------------------------------------------

def retrieve_federate(user_key, federate_name):

    # if database does not exist within directory raise an exception
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    client_profile = get_profiles({"key": user_key})
    
    # Only members of a federate can access worker information
    if not (client_profile) or not (client_profile[0]["federate"] == federate_name):
        raise Exception("You do not have permission to look up a federation")

    with connect(DATABASE_URL, uri=True) as connection:
        connection.row_factory = Row

        # Return a list of matching profiles
        with closing(connection.cursor()) as cursor:
            sql_statement = 'SELECT name, federate, email, location, age, role FROM profiles '
            sql_statement += "WHERE federate LIKE ? "
            cursor.execute(sql_statement, [federate_name])
            row_list = [dict(row) for row in cursor.fetchall()]

            # if empty list then no such federate exists
            if not row_list:
                raise Exception("Federate doesn't exist")

            return row_list

#-----------------------------------------------------------------------

if __name__ == "__main__":
    print(retrieve_federate("12345", "The Driver's Coop"))