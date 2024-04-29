import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
import sqlite3
from datetime import datetime

# Set up the RFID reader
reader = SimpleMFRC522()

# Set up the I2C LCD
lcd = CharLCD('PCF8574', 0x27)

# Connect to the SQLite database
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Create a table to store student attendance
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (regno VARCHAR, date DATE)''')
conn.commit()

def debug_lcd(message):
    print("[LCD]:", message)

def read_from_rfid():
    debug_lcd("Hold a tag near the RFID reader")
    id, text = reader.read()
    text = text.strip()  # Remove leading and trailing spaces
    debug_lcd("Data: %s" % text)

    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Insert the attendance data into the database
    cursor.execute("INSERT INTO students VALUES (?, ?)", (text, current_date))
    conn.commit()

    # Display data on the LCD
    lcd.clear()
    lcd.write_string("RegNo: %s" % text)
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Date: %s" % current_date)

def write_to_rfid():
    data_to_write = input("Enter the data to write to the RFID tag: ").strip()
    debug_lcd("Now, hold your RFID tag near the RFID reader to write the data.")

    reader.write(data_to_write)
    debug_lcd("Data has been written to the RFID tag.")

    lcd.clear()
    lcd.write_string("Write Successful")

def main():
    while True:
        debug_lcd("Choose an option:")
        debug_lcd("1. Read from RFID")
        debug_lcd("2. Write to RFID")
        debug_lcd("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            read_from_rfid()
        elif choice == "2":
            write_to_rfid()
        elif choice == "3":
            debug_lcd("Exiting the program")
            break
        else:
            debug_lcd("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    finally:
        conn.close()
        GPIO.cleanup()
