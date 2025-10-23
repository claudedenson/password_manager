import os
import rot3
import re

# File
FILE_NAME = "credentials.txt"

# Create a text file for credential storage if a text file does not already exist 
def store_credentials():
    print(f"Enter your credentials...\n")

    username = input("Enter your username:")
    password = input("Enter your password:")
    url = input("Enter URL/resource:")
    
    encrypted_password = rot3.rot3_cypher(password, 3)

    if os.path.exists(FILE_NAME):
        # Add new record
        with open(FILE_NAME, "a") as file:
            file.write(f"{username},{encrypted_password},{url}\n")
    
        print(f"New record added successfully.")

    else:
        print(f"The file '{FILE_NAME}' does not exist. It will be created.")
        
        # Creates file
        new_file = open(FILE_NAME, "x")
        
        print(f"File '{new_file}' created successfully.")

         # Add new record
        with open(FILE_NAME, "a") as file:
            file.write(f"{username},{encrypted_password},{url}\n")

def view_credentials():
    print(f"\nView stored credentials in {FILE_NAME}...\n") 

    # Display the text file contents
    with open(FILE_NAME, "r") as file:
        for line in file.readlines():
            data = re.split(",", line)
            print(f"username: {data[0]}, password: {rot3.rot3_cypher(data[1], -3)}, url: {data[2]}")