import os
import rot3

# File
file_name = "credentials.txt"

# Create a text file for credential storage if a text file does not already exist 
def store_credentials():
    print(f"\nAdd stored credentials...\n")
    new_record = input("Enter your credentials:")
    encrypted_record = rot3.rot3_encrypt(new_record)

    if os.path.exists(file_name):
        # Add new record
        with open(file_name, "a") as file:
            file.write(f"{encrypted_record}\n")

        print(f"New record added successfully.")

    else:
        print(f"The file '{file_name}' does not exist. It will be created.")
        
        # Creates file
        new_file = open(file_name, "x")
        
        print(f"File '{new_file}' created successfully.")

def view_credentials():
    print(f"\nView stored credentials in {file_name}...\n") 

    # Display the text file contents
    with open(file_name, "r") as file:
        print(rot3.rot3_decrypt(file.read()))