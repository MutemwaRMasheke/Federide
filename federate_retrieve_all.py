#-----------------------------------------------------------------------
# profiles_query.py
# Author: Mutemwa Masheke 
#-----------------------------------------------------------------------

import os.path
from contextlib import closing
from sqlite3 import connect, Row

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = 'federide.sqlite'

#-----------------------------------------------------------------------
def retrieve_all_federate(args={}):
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    with connect(DATABASE_URL, uri=True) as connection:
        connection.row_factory = Row
        with closing(connection.cursor()) as cursor:
            sql_args = []
            sql_statement = 'SELECT federate FROM profiles '
            if args and ("location" in args.keys()):
                sql_statement += "WHERE location LIKE ? "
                sql_args.append(args["location"])
            cursor.execute(sql_statement, sql_args)
            row_list = set([dict(row)["federate"] for row in cursor.fetchall()])
            row_list = list(row_list)
            
            if not row_list:
                raise Exception("Federate doesn't exist")

            return row_list

#-----------------------------------------------------------------------

if __name__ == "__main__":
    print(retrieve_all_federate({"location": "Lusaka"}))