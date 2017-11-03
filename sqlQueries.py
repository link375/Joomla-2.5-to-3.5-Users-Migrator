import db

# QUERY DATA

# query to select all user data from the joomla 2.5 db
db.firstDB_c.execute("""SELECT * FROM #_users""")

# query to select all user data from the joomla 3.5 db
db.secondDB_c.execute("""SELECT * FROM #_users""")

# store all results from the query
results_firstDB = db.firstDB_c.fetchall()
results_secondDB = db.secondDB_c.fetchall() 



# INSERT DATA

# Insert query when you are writing to the joomla 3.5 db
insert_row = "INSERT INTO test_users(name, username, email, password, block, sendEmail, \
                 registerDate, lastvisitDate, activation, params, lastResetTime, \
               resetCount, otpKey, otep, requireReset) \
              VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"