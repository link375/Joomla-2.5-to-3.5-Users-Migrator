import db

# QUERY DATA

db.firstDB_c.execute("""SELECT * FROM #_users""")
db.secondDB_c.execute("""SELECT * FROM #_users""")

# store all results from the query
results_firstDB = db.firstDB_c.fetchall()
results_secondDB = db.secondDB_c.fetchall()


# INSERT DATA

insert_row = "INSERT INTO test_users(name, username, email, password, block, sendEmail, \
                 registerDate, lastvisitDate, activation, params, lastResetTime, \
               resetCount, otpKey, otep, requireReset) \
              VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"