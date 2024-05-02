from flask import Flask, render_template, request
import sqlite3
import subprocess

app = Flask(__name__)

# Function to query the SQLite database
def query_attendance(regno, required_date):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()

    # Query for total attendance
    c.execute("SELECT COUNT(DISTINCT date) FROM students WHERE regno = ?", (regno,))
    total_attendance = c.fetchone()[0]

    # Query for present on required date
    c.execute("SELECT COUNT(*) FROM students WHERE regno = ? AND date = ?", (regno, required_date))
    present_on_required_date = c.fetchone()[0]

    conn.close()

    return total_attendance, present_on_required_date

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attendance', methods=['POST'])
def get_attendance():
    regno = request.form['regno']
    required_date = request.form['date']
    total_attendance, present_on_required_date = query_attendance(regno, required_date)
    
    # Calculate percentage attendance
    percentage_attendance = (total_attendance /5) * 100

    if percentage_attendance < 75:
            subprocess.run(["python", "send.py", regno])
        
    # Format present on required date
    present_status = "Present" if present_on_required_date>0 else "Absent"

    return render_template('index.html', regno=regno, percentage_attendance=percentage_attendance, present_status=present_status)

if __name__ == '__main__':
    app.run(debug=True)
