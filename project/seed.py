import sqlite3
from datetime import datetime, timedelta
import os
import random

try:
    # Connect to the database
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()

    # Create the students table if it doesn't exist
    # c.execute('''CREATE TABLE IF NOT EXISTS students (
    #                 regno VARCHAR,
    #                 date DATE
    #              )''')

    # # Clear the existing records in the students table
    # c.execute("DELETE FROM students")

    # # Define the list of registration numbers
    # registration_numbers = ['21BPS1263', '21BAI1660', '21BCE5335', '21BCE5537', '21BRS1469']

    # # Define the date range
    # start_date = datetime(2024, 4, 14).date()  # Start date: April 14, 2024
    # end_date = start_date + timedelta(days=4)  # End date: April 18, 2024

    # # Insert records for each registration number on random dates
    # for regno in registration_numbers:
    #     dates_to_insert = [date for date in (start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1))]
    #     # Remove April 17 from the list of dates
    #     if datetime(2024, 4, 17).date() in dates_to_insert:
    #         dates_to_insert.remove(datetime(2024, 4, 17).date())
    #         # Randomly select a subset of dates to insert
    #     dates_to_insert = random.sample(dates_to_insert, random.randint(1, len(dates_to_insert)))
    #     # Insert records for the selected dates
    #     for date in dates_to_insert:
    #         c.execute("INSERT INTO students (regno, date) VALUES (?, ?)", (regno, date))

    # Delete records with the date '2024-04-21'
    c.execute("DELETE FROM students WHERE date = ?", ('2024-04-21',))
    
    # Insert the record
    # regno = '21BPS1263'
    # date = '2024-04-23'  # Date format: YYYY-MM-DD
    # c.execute("INSERT INTO students (regno, date) VALUES (?, ?)", (regno, date))  

    # Commit the transaction
    conn.commit()
    print("Records inserted successfully.")

except sqlite3.Error as e:
    print("SQLite error:", e)

finally:
    # Close the connection
    conn.close()


