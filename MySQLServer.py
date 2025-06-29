#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

try:
    # connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',       # غيرها لو عندك سيرفر تاني
        user='root',            # يفضل تحط يوزر مناسب
        password='your_password' # غيرها بالباسورد بتاعك
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # create database with IF NOT EXISTS
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

