import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Create the students table
cursor.execute('''CREATE TABLE IF NOT EXISTS info (
                    regno VARCHAR PRIMARY KEY,
                    email TEXT
                  )''')

# cursor.execute("DROP TABLE IF EXISTS info")

# Sample data
data = [
    ('21BPS1263', 'devansh.mathur2021@vitstudent.ac.in'),
    ('21BAI1660', 'hrishikesh.gkulkarni2021@vitstudent.ac.in'),
    ('21BCE5335', 'ayush.2021c@vitstudent.ac.in'),
    ('21BCE5537', 'soma.anirudh2021@vitstudent.ac.in'),
    # add more data as needed
]

# Insert data into the students table
for entry in data:
    cursor.execute("INSERT INTO info (regno, email) VALUES (?, ?)", entry)


# Commit the transaction
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
