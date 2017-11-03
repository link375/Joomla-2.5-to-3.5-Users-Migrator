# Joomla 2.5 - 3.5 User Migrator
 This program will help you merge a joomla 2.5 users table with a joomla 3.5 users table
 the result will be written to the joomla 3.5 table all usernames and emails will be checked
 there will not be any overlapping results new entries will be written with auto-incrementing ids

# instructions
- MAKE A BACKUP OF YOUR 2 DATABASES! DON'T BE STUPID!
- setup the db.py file to match your 2 databases
- check the sqlQueries.py file to make sure you are querying the correct tables
- check the sqlQueries.py file to make sure you are INSERTING into the correct table
- run
- profit

# Dependencies

Python 3.5x

# Libraries

- csv

- mysql-client

- MySQLdb

- datetime


