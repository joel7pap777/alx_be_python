#!/usr/bin/python3
"""Creates the database alx_book_store in a MySQL server."""

import mysql.connector

db = None
cursor = None

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Joel200507$"
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if cursor is not None:
        cursor.close()
    if db is not None:
        db.close()

