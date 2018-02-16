import db
import csv
import functions as utilities
import sqlQueries as Query

# convert tuples to lists so they can be modified
firstDB_list = list(Query.results_firstDB)
secondDB_list = list(Query.results_secondDB)

# create a list of items without and index
# we will use this to compare each row to all items in this list
secondDB_items = utilities.extract_items(secondDB_list)

# find all unique users
uniqueUsersList = utilities.find_unique_users(firstDB_list, secondDB_items)

# remove joomla 2.5 headings and insert joomla 3.5 headings and values
final = utilities.create_final(uniqueUsersList)

# insert the final list to the test database
db.test_c.executemany(Query.insert_users_row, final)
db.testDB.commit()

# query the test database for the users that have not logged in yet
thirdDB_list = list(Query.queryUser_userGroup())

# add the usergroup permissions to the list of users
usergroup_map_list = utilities.addUserGroup(thirdDB_list)

# add the usergroup permissions to the test database
db.test_c.executemany(Query.insert_usergroup_map_row, usergroup_map_list)
db.testDB.commit()

# close database connection
db.testDB.close()

# create a csv file and write final list to it
with open("users.csv", "w", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)

    # write the headings to the csv file based on the joomla 3.5 headings
    csv_writer.writerow(Query.headings)

    # write the final rows
    csv_writer.writerows(final)

