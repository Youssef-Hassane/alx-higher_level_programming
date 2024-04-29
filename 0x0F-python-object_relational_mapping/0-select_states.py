#!/usr/bin/python3


import MySQLdb as db  # Renamed to db for brevity
from sys import argv as args  # Renamed to args for brevity

'''
Script to list all states from the database.
'''

if __name__ == "__main__":
    # Establish connection
    conn = db.connect(host="localhost", port=3306,
                      user=args[1], password=args[2],
                      database=args[3])

    # Create cursor
    cursor = conn.cursor()

    # Execute SQL statement
    cursor.execute("""
        SELECT * FROM states ORDER BY id ASC
    """)

    # Fetch all records
    records = cursor.fetchall()

    # Print each record
    for record in records:
        print(record)

    # Close cursor and connection
    cursor.close()
    conn.close()
