import MySQLdb

# DATABASE INFORMATION
host = "your_host.com"
user = "your_db_user"
password = "your_db_password"

# ORIGINAL DATABASE - joomla 2.5
joomlaTwoDB = "your_joomla_2.5_schema"

# SECOND DATABASE - joomla 3.5
JoomlaThreeDB = "your_joomla_3.5_schema"


# connect to the db
# joomla 2.5
firstDB = MySQLdb.connect(host=host,
                          user=user,
                          passwd=password,
                          db=joomlaTwoDB)

# joomla 3.5
secondDB = MySQLdb.connect(host=host,
                           user=user,
                           passwd=password,
                           db=JoomlaThreeDB)


# create a cursor
firstDB_c = firstDB.cursor()
secondDB_c = secondDB.cursor()


#########TESTING##########

joomlaTestDB = "your_test_schema"

testDB = MySQLdb.connect(host=host,
                         user=user,
                         passwd=password,
                         db=joomlaTestDB)

test_c = testDB.cursor()
