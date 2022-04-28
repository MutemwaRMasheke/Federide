#-----------------------------------------------------------------------
# profiles_get.py
# Author: Mutemwa Masheke
# 
# Retrieves a profile using name, federate, email, location, age, role 
# information
#-----------------------------------------------------------------------

from operator import contains
import os.path
from contextlib import closing
from sqlite3 import connect, Row

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = 'federide.sqlite'

#-----------------------------------------------------------------------
def get_profiles(args):
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    with connect(DATABASE_URL, uri=True) as connection:
        connection.row_factory = Row
        with closing(connection.cursor()) as cursor:
            sql_statement, sql_args = _list_query_builder(args)
            cursor.execute(sql_statement, [arg.replace("'", "") for arg in sql_args])
            row_list = [dict(row) for row in cursor.fetchall()]
            return row_list

#-----------------------------------------------------------------------

# builds the query by adding arguments to the query statement
def _stmt_append(statement, arg_list, arg_type, arg_string):
    if "WHERE" not in statement:
        statement ='{0} WHERE {1} LIKE ? '.format(statement, arg_type)
    else:
        statement ='{0} AND {1} LIKE ? '.format(statement, arg_type)
    arg_list.append('{0}'.format(arg_string))
    return statement, arg_list

#-----------------------------------------------------------------------

# creates entire database query
def _list_query_builder(query_info):
    # Building the query string using predefined statements
    sql_args = []
    stmt_str = 'SELECT name, federate, email, location, key, age, role FROM profiles'

    for key in query_info.keys():
        stmt_str, sql_args = _stmt_append(stmt_str, sql_args, \
            key, query_info[key])

    # defining escape character to be a backslash
    if any([arg and not arg.isspace() for arg\
         in query_info.values()]):
        stmt_str += 'ESCAPE \'\\\' '

    # close off query
    stmt_str += 'ORDER BY name, federate, role, location, email, key, age'
    return stmt_str, sql_args

#-----------------------------------------------------------------------

if __name__ == "__main__":
    print(get_profiles({
        "name": 'Mutemwa Masheke',
    }))