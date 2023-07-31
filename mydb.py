import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2541muriithi",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE dcrm")
print("Database created successfully")