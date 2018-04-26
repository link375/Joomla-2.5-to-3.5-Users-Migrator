import db

# QUERY DATA

# query to select all user data from the joomla 2.5 db
db.firstDB_c.execute("""SELECT * FROM <changeme_db2.5>_users""")

# query to select all user data from the joomla 3.5 db
db.secondDB_c.execute("""SELECT * FROM <changeme_db3.5>_users""")

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
    db.secondDB_c.execute('''SELECT id FROM <changeme_joomla3.5>_users WHERE lastResetTime="2018-04-12 00:00:00"''')
    results = db.secondDB_c.fetchall()
    return results