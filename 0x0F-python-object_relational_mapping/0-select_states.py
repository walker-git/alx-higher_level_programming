#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Open database connection
    db = MySQLdb.connect("localhost", username, password, db_name)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows using fetchall() method.
    results = cursor.fetchall()

    # print the results
    for row in results:
        print(row)

    # disconnect from server
    db.close()

