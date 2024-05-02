import sqlite3
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route to display the attendance data
@app.route('/')
def index():
    # Connect to the SQLite database
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    # Fetch all student attendance records
    cursor.execute("SELECT * FROM students")
    attendance_records = cursor.fetchall()
    print(attendance_records)

    # Close the database connection
    cursor.execute("SELECT * from info")
    email_info = cursor.fetchall()
    conn.close()

    return render_template('index.html', attendance_records=attendance_records, email_info=email_info)

if __name__ == '__main__':
    app.run()