#-----------------------------------------------------------------------
# profiles_edit.py
# Author: Mutemwa Masheke
# 
# Alters a profile given a key using name, federate, email, location, age, role 
# information
#-----------------------------------------------------------------------

from profiles_create import create_profile
from profiles_get import get_profiles
from operator import contains
import os.path
from contextlib import closing
from sqlite3 import connect

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = 'federide.sqlite'

#-----------------------------------------------------------------------
def edit_profile(user_key, args):
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:
            queried_profiles = get_profiles({"key": user_key})

            # nothing to edit if profile doesnt exist
            if not queried_profiles:
                raise Exception('User does not exist')

            # Delete existing profile
            sql_statement = "DELETE FROM profiles WHERE key LIKE ?"
            cursor.execute(sql_statement, [user_key]) 

            # Edit existing information
            edited_profile = queried_profiles[0]
            for arg in args:
                edited_profile[arg] = args[arg]

            # Create new one with updated information
            sql_statement, sql_args = _profile_builder(edited_profile)
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
    edit_profile("12345", {
        "name": "Mutemwa Masheke",
        "location": "London",
        "federate": "The Driver's Coop",
    })