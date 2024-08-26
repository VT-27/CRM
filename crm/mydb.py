# install mysql on this mac
# pip install mysql
# pip install mysql-connector
# pip intall mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Vivek@2709'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a DB
cursorObject.execute("Create DATABASE elderco")
print("All DOne")