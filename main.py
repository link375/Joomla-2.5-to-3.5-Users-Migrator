import vars as a
import MySQLdb
import csv

# connect to the db
second_db=MySQLdb.connect(host=a.host, user=a.user,
                passwd=a.password, db=a.second_db)

first_db=MySQLdb.connect(host=a.host, user=a.user,
                passwd=a.password, db=a.first_db)


# create a SQL cursor
second_c = second_db.cursor()
first_c = first_db.cursor()

# execute query
second_c.execute("""SELECT * FROM users""")
first_c.execute("""SELECT * FROM users""")

# store all results from the query
results_second = second_c.fetchall()
results_first = first_c.fetchall()

# convert tuples to lists so they can be modified
second_list = list(results_second)
first_list = list(results_first)


def extract_items(list):
    """extract all items from a list and put them into a new list"""

    # create an empty list to store results
    items = []

    # iterate through rows in the list
    for row in list:
        # iterate through items in the row
        for item in row:
            # add item to items list
            items.append(item)
    # return the full array
    return items


# create a list of items without an index
second_items = extract_items(second_list)

# create a csv file and writer
with open("users.csv", "w") as csvfile:
    csv_writer = csv.writer(csvfile)

    # id = 0
    # user = 2
    # email = 3

    # write the headings to the csv file based on the old database
    csv_writer.writerow([i[0] for i in second_c.description])

    # create a new list to store unique users
    unique_users = []

    for row in first_list:  # iterate through the list one row at a time (original site)
        for item in row:  # iterate through items in each row one item at a time
            if row[0] in second_items:  # if id is found in ce_items move on to the next item
                continue
            elif row[2] in second_items: # if username is found in ce_item move on to the next item
                continue
            elif row[3] in second_items: # if email is found in ce_items move on to the next item
                continue
            else:  # otherwise break out of this loop and return to the first one
                unique_users.append(row) # write the current row to the unique users list
                break # break out of the primary loop

    # once we're back on the main loop we can write the current row to the csv file
    csv_writer.writerows(unique_users)


