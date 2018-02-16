import db

# QUERY DATA

# query to select all user data from the joomla 2.5 db
db.firstDB_c.execute("""SELECT * FROM <changeme>_users""")

# query to select all user data from the joomla 3.5 db
db.secondDB_c.execute("""SELECT * FROM <changeme>_users""")

# store all results from the query
results_firstDB = db.firstDB_c.fetchall()
results_secondDB = db.secondDB_c.fetchall() 



# INSERT DATA

# Insert query when you are writing to the joomla 3.5 db
insert_users_row = "INSERT INTO <changeme_db3.5>_users(name, username, email, password, block, sendEmail, \
                 registerDate, lastvisitDate, activation, params, lastResetTime, \
               resetCount, otpKey, otep, requireReset) \
              VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_usergroup_map_row = "INSERT INTO <changeme_db3.5>_user_usergroup_map(user_id, group_id) \
                           VALUES(%s, %s)"

#CSV headings
headings = "name", "username", "email", "password", "block", "sendEmail", \
           "registerDate", "lastvisitDate", "activation", "params", "lastResetTime", \
           "resetCount", "otpKey", "otep", "requireReset"


def queryUser_userGroup():
    db.test_c.execute("""SELECT id FROM <changeme_db3.5>_users WHERE lastvisitDate = '0000-00-00 00:00:00'""")
    results_thirdDB = db.test_c.fetchall()
    return results_thirdDB