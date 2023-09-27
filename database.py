import mysql.connector

mydb = mysql.connector.connect(user="root",
                               password="",
                               host="127.0.0.1",
                               database="first my_database")

cursor = mydb.cursor()

sql = """" CREATE TABLE definition(
        def_id INTEGER INTEGER NOT NULL PRIMARY KEY,
        title CHARFIELD(100)
        category BINARY(1)
        def_text VARCHAR()
        )"""

sql = """" CREATE TABLE organization(
        org_id INTEGER NOT NULL PRIMARY KEY,
        title CHARFIELD(100)
        name_proces VARCHAR(100) NOT NULL,
        child_id INTEGER()
        org_name CARFIELD() NOT NULL,
        org_task VARCHAR() NOT NULL,
        parent_id INTEGER NOT NULL PRIMARY KEY,
        org_type BINARY(1)

        )"""

sql = """" CREATE TABLE status(
        parent_id INTEGER INTEGER NOT NULL PRIMARY KEY,
        parent_name CHARFIELD(100)
        child_id INTEGER()
        child_name CHARFIELD()
        )"""
sql = """" CREATE TABLE laws_doc(
        laws_id INTEGER INTEGER NOT NULL PRIMARY KEY,
        made INTEGER()
        tabsare VARCHAR()
        org_id INTEGER()
        )"""
cursor.execute("CREATE DATABASE")
result = cursor.fetchall()
print(result)
mydb.commit()
print(cursor.rowcount, "record_inserted")
