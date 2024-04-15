import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an instance of the MFRC522 class
MIFAREReader = MFRC522.MFRC522()

# Function to read from NFC card
def read_card():
    print("Place your card near the reader...")
    # This loop keeps checking for RFID tags
    while continue_reading:
        # Scan for cards
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print("Card detected")

        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            # Print UID
            print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
            break

# Function to write to NFC card
def write_card():
    print("Place your card near the reader...")
    # This loop keeps checking for RFID tags
    while continue_reading:
        # Scan for cards
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print("Card detected")

        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            # Print UID
            print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
            # Write data to the card
            data = input("Enter data to write to the card: ")
            MIFAREReader.MFRC522_Write(8, data.encode())
            print("Data has been written to the card.")
            break

# Main loop
while True:
    print("\nChoose an option:")
    print("1. Read from NFC card")
    print("2. Write to NFC card")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        read_card()
    elif choice == '2':
        write_card()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

