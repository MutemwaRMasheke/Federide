#-----------------------------------------------------------------------
# federate_retreive_all.py
# Author: Mutemwa Masheke
# 
# Deletes an entire federate from the profile database and remove all 
# workers from the storage. Returns a csv file with the deleted 
# information 
#-----------------------------------------------------------------------

import os.path
from contextlib import closing
from sqlite3 import connect, Row

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = 'federide.sqlite'

#-----------------------------------------------------------------------

# retrieves an entire list of all federate coops 
def retrieve_all_federate(args={}):

    # if database does not exist within directory raise an exception
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    
    with connect(DATABASE_URL, uri=True) as connection:
        connection.row_factory = Row

        # return a list of names of federates
        with closing(connection.cursor()) as cursor:
            sql_args = []
            sql_statement = 'SELECT federate FROM profiles '

            # optionally select location
            if args and ("location" in args.keys()):
                sql_statement += "WHERE location LIKE ? "
                sql_args.append(args["location"])

            cursor.execute(sql_statement, sql_args)
            row_list = set([dict(row)["federate"] for row in cursor.fetchall()])
            row_list = list(row_list)
            
            # if empty list then no such federate exists
            if not row_list:
                raise Exception("Federate doesn't exist")

            return row_list

#-----------------------------------------------------------------------

if __name__ == "__main__":
    print(retrieve_all_federate({"location": "Lusaka"}))