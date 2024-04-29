#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to database
    db_host = "localhost"
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    db_charset = "utf8"

    # Establish connection to database
    db_connection = MySQLdb.connect(
        host=db_host, port=3306, user=db_user, passwd=db_passwd,
        db=db_name, charset=db_charset)

    # Create cursor to execute query
    db_cursor = db_connection.cursor()

    # Execute query
    query = ("SELECT cities.id, cities.name, states.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    db_cursor.execute(query)

    # Print rows
    for db_row in db_cursor.fetchall():
        # Print city information
        city_id, city_name, state_name = db_row
        print("City ID: {}, City Name: {}, State Name: {}"
              .format(city_id, city_name, state_name))

    # Close cursor and connection
    db_cursor.close()
    db_connection.close()
