import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user='root',
    password='iammacrm',
)

#prepare a cursor object
cursorObject= dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE crm_project")

print("All done")