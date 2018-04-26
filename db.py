import MySQLdb

# ORIGINAL DATABASE INFO
host = "your_joomla2.5_host"
user = "your_joomla2.5_db_user"
password = "your_joomla2.5_db_password"

# ORIGINAL DATABASE - joomla 2.5
joomlaTwoDB = "your_joomla_2.5_schema"

# connect to the db
# joomla 2.5
firstDB = MySQLdb.connect(host=host,
                          user=user,
                          passwd=password,
                          db=joomlaTwoDB)

# create a cursor
firstDB_c = firstDB.cursor()


# DESTINATION DATABASE INFO
host2 = "your_joomla3.5_db_host"
user2 = "your_joomla3.5_db_user"
password2 = "your_joomla3.5_db_password"

# SECOND DATABASE - joomla 3.5
JoomlaThreeDB = "your_joomla_3.5_schema"

# connect to the db
# joomla 3.5
secondDB = MySQLdb.connect(host=host2,
                           user=user2,
                           passwd=password2,
                           db=JoomlaThreeDB)

# create a cursor
secondDB_c = secondDB.cursor()
