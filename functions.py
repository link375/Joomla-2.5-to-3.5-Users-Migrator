import datetime

# functions and utilities for the main program


def extract_items(list):
    """extract all items from a database list and put them into a new list without an index to reference"""

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


def find_unique_users(dblist, items):
    """Run through both databases and compare values"""

    # create a list to return
    uniqueUsers = []

    # no magic numbers! column values
    # id = 0
    user = 2
    email = 3

    # check each row then check each item in a row
    for row in dblist:
        for item in row:
            if row[user] in items:
                continue
            elif row[email] in items:
                continue
            else:
                uniqueUsers.append(row)
                break
    return uniqueUsers


def create_final(uniqueUsers):
    """Create a cleaned up list of users with joomla 3.5 formatting"""

    # create a final list
    final = []

    # go through the unique users and strip it of joomla 2.5 columns
    for row in uniqueUsers:

        # enumarate
        newId = 0
        id = 0
        password = 4
        usertype = 5
        block = 6
        sendEmail = 7
        registerDate = 8
        lastvisitDate = 9
        activation = 10
        params = 11
        lastResetTime = 12
        resetCount = 13

        # usertype is only found on joomla 2.5
        # if usertype is found then remove all of the columns
        if row[usertype] == "Registered"\
            or row[usertype] == "Super Users"\
            or row[usertype] == "Administrator"\
            or row[usertype] == "Public Frontend"\
            or row[usertype] == "2"\
            or row[usertype] == "":
                # create a temporary list because tuples can't be modified
                temp_row = list(row)
                # remove the columns from greatest to least to avoid messing up data
                temp_row.remove(row[resetCount])
                temp_row.remove(row[lastResetTime])
                temp_row.remove(row[params])
                temp_row.remove(row[activation])
                temp_row.remove(row[lastvisitDate])
                temp_row.remove(row[registerDate])
                temp_row.remove(row[sendEmail])
                temp_row.remove(row[block])
                temp_row.remove(row[usertype])
                temp_row.remove(row[password])
                # strip the id since it will be auto incremented
                temp_row.remove(row[id])
                # assign the new clean list back to the row
                row = tuple(temp_row)

        # Define item values for each column on joomla 3.5 db
        # Default password: password123456!
        password = "$2y$10$JQqeCoAukw5wzzfxcWzebeOAzDcNxqtne8enZbqTYrUCQmNw.05Na"
        block = '0'
        sendEmail = '0'
        registerDate = str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        lastvisitDate = "0000-00-00 00:00:00"
        activation = ''
        params = '{"language":"en-GB"}'
        lastResetTime = "0000-00-00 00:00:00"
        resetCount = '0'
        otpKey = ''
        otep = ''
        requireReset = '0'

        # append the values above to the new clean row that contains only id, name, user, email, password
        row = row + (password, block, sendEmail, registerDate, lastvisitDate, activation, params,
                     lastResetTime, resetCount, otpKey, otep, requireReset)

        # add the newly formatted row to the final list
        final.append(row)
        # go back and run through the next row - at the end return the final list

    return final

def addUserGroup(thirdDBList):
    """append a 2 to mark the user as a registered user"""
    user_id = 0
    group_id = 2
    idList = []

    for row in thirdDBList:
        row = row + (group_id,)
        idList.append(row)
    return idList

