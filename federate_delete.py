#-----------------------------------------------------------------------
# profiles_query.py
# Author: Mutemwa Masheke 
#-----------------------------------------------------------------------

from profiles_get import get_profiles
import csv
import os.path
from contextlib import closing
from sqlite3 import connect

#-----------------------------------------------------------------------

DATABASE_URL = 'file:federide.sqlite'
DB_FILENAME = 'federide.sqlite'

#-----------------------------------------------------------------------
def delete_federate(user_key, federate_name):
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')

    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:
            client_profile = get_profiles({"key": user_key})

            if not client_profile:
                raise Exception("You do not have permission to delete a federation")

            validate_profile = client_profile[0]

            if not (validate_profile["federate"] == federate_name) and ("account" in validate_profile["role"]):
                raise Exception("You do not have permission to delete a federation")

            federate_csv = get_profiles({"federate": federate_name})

            sql_statement = "DELETE FROM profiles WHERE federate LIKE ?"
            cursor.execute(sql_statement, [federate_name])

            return federate_csv

#-----------------------------------------------------------------------
def createCSV(dictionary_list, csv_name):
    columns = list({key for dictionary in dictionary_list for key in dictionary.keys()})
    
    with open(csv_name.append(".csv",""), 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = columns)
        writer.writeheader()
        writer.writerows(dictionary_list)

    return csvfile

#-----------------------------------------------------------------------

if __name__ == "__main__":
    print(delete_federate("12345", "The Driver's Coop"))