from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
from time import sleep

# Initialize the LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

reader = SimpleMFRC522()

# Function to read from RFID card
def read_from_card():
   try:
       lcd.cursor_pos = (0, 0)
       lcd.write_string("Hold card near")
       lcd.cursor_pos = (1, 0)
       lcd.write_string("reader... ")
       print("Hold your card near the reader...")
       id, text = reader.read()
       print("Card detected")
       if id is not None:
           lcd.cursor_pos = (0, 0)
           lcd.write_string("Read successful!")
           lcd.cursor_pos = (1, 0) # Setting cursor position
           if text:
               lcd.write_string(str(text))
           return id, text
   except KeyboardInterrupt:
       print("Operation aborted by user.")
       return None, None

# Function to write to RFID card
def write_to_card(data):
   try:
       lcd.write_string("Hold card near")
       lcd.cursor_pos = (1, 0)
       lcd.write_string("reader...       ")
       print("Hold your card near the reader...")
       print("Writing data to the card...")
       reader.write(data)
       print("Data has been written successfully!")
   except KeyboardInterrupt:
       print("Operation aborted by user.")

# Main function
def main():
   while True:
       # Display menu on LCD
       lcd.cursor_pos = (0, 0)
       lcd.write_string("0-Read 1-Write")
       lcd.cursor_pos = (1, 0)
       lcd.write_string("2-Exit")

       # Wait for user input
       key = input("Enter your choice (0/1/2): ")

       if key == '0':
           read_from_card()
           sleep(5)
       elif key == '1':
           data = input("Enter data to write to the card: ")
           write_to_card(data)
           lcd.clear()
           lcd.write_string("Write successful!")
           sleep(5)
       elif key == '2':
           break

if __name__ == "__main__":
   try:
       main()
   finally:
       # Perform any necessary cleanup here
       pass
