import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2541muriithi",
    database="dcrm",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrm")
print("Database created successfully")
