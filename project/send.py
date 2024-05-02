import subprocess
import sqlite3
import sys  # Import sys module to access command line arguments

def get_email_from_db(regno):
    # Connect to the SQLite database (attendance.db)
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    # Execute a query to select the email associated with the regno
    cursor.execute("SELECT email FROM info WHERE regno = ?", (regno,))
    result = cursor.fetchone()  # Fetch the first result

    if result:
        email = result[0]  # Extract the email from the result
    else:
        email = None  # Return None if regno is not found

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    return email

if __name__ == "__main__":
    regno = sys.argv[1]  # Get the regno from command line arguments
    email = get_email_from_db(regno)
    if email:
        print("Sending notification to email:", email)
        # Execute send_email.py script to send email
        subprocess.run(["python", "send_email.py", email])
    else:
        print("Email not found for regno:", regno)



# import os 
# from email.message import EmailMessage
# import ssl 
# import smtplib
# email_sender = 'hrishikeshbrawlstars009@gmail.com'
# email_password = 'ugfh acdr lcxu zsrd'

# email_receiver = 'devansh.mathur2021@vitstudent.ac.in'

# subject = 'Attendance Low'
# body = "Please take care of your attendance it is below 75% now"

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())




