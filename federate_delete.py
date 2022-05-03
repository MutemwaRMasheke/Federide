#-----------------------------------------------------------------------
# federate_delete.py
# Author: Mutemwa Masheke
# 
# Deletes an entire federate from the profile database and remove all 
# workers from the storage. Returns a csv file with the deleted 
# information 
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

# Takes a user account key and deletes all workers from a federation only if the user 
# account has permission to do so. Returns a csv file of all federation members
def delete_federate(user_key, federate_name):

    # if database does not exist within directory raise an exception
    if not os.path.isfile(DB_FILENAME):
        raise Exception('unable to open database file')


    with connect(DATABASE_URL, uri=True) as connection:
        with closing(connection.cursor()) as cursor:

            client_profile = get_profiles({"key": user_key})
             
            # ensure user key exists
            if not client_profile:
                raise Exception("You do not have permission to delete a federation")

            validate_profile = client_profile[0]

            # user has to have adequate permissions to make delete permission
            if not (validate_profile["federate"] == federate_name) and ("account" in validate_profile["role"]):
                raise Exception("You do not have permission to delete a federation")

            # create csv of deleted data
            federate_csv = get_profiles({"federate": federate_name})

            sql_statement = "DELETE FROM profiles WHERE federate LIKE ?"
            cursor.execute(sql_statement, [federate_name])

            return federate_csv

#-----------------------------------------------------------------------

# takes in an array of profiles and returns a csv file
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