#-----------------------------------------------------------------------
# profiles_query.py
# Author: Mutemwa Masheke 
#-----------------------------------------------------------------------

from profiles_get import get_profiles
import os.path
from contextlib import closing
from sqlite3 import connect

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = 'federide.sqlite'

#-----------------------------------------------------------------------
def create_profile(args):
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    if (args["role"] == "patron" and args["federate"]):
        raise Exception('patron cannot be a member of a federate')

    if get_profiles({"key": args["key"]}):
        raise Exception('User already exists')

    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:
            sql_statement, sql_args = _profile_builder(args)
            cursor.execute(sql_statement, sql_args)

#-----------------------------------------------------------------------

# creates entire database query
def _profile_builder(query_info):
    # Building the query string using predefined statements

    keys = ", ".join(query_info.keys())
    question_marks = ", ".join(["?" for i in query_info.keys()])
    sql_args = [i for i in query_info.values()]
    stmt_str = f'''INSERT INTO profiles ({keys}) VALUES ({question_marks}) '''

    return stmt_str, sql_args

#-----------------------------------------------------------------------

if __name__ == "__main__":
    create_profile({
        "name": "Mutemwa Masheke",
        "location": "Lusaka",
        "role": "account_manager",
        "federate": "The Driver's Coop",
        "email": "mmasheke@princeton.edu",
        "key": "12345",
        "age": "21"
    })