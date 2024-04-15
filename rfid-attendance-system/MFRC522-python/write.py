from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    # Prompt the user to input data to write to the card
    text = input("Enter data to write to the card: ")
    
    # Write data to the RFID card
    print("Hold your card near the reader to write data...")
    reader.write(text)
    print("Data has been written successfully!")
finally:
    # Cleanup the GPIO pins
    reader.cleanup()

