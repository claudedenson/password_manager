import os

# Give the user some context. 
print("\n==== Simple Password Manager ====") 

# File
file_name = "credentials.txt"

# Create a text file for credential storage if a text file does not already exist 
def store_credentials():
    print(f"\nAdd stored credentials...\n")
    new_record = input("Enter your credentials:")
    encrypted_record = rot3_encrypt(new_record)

    if os.path.exists(file_name):
        # Add new record
        with open(file_name, "a") as file:
            file.write(f"{encrypted_record}\n")

    else:
        print(f"The file '{file_name}' does not exist. It will be created.")
        
        # Creates file
        new_file = open(file_name, "x")
        
        print(f"File '{new_file}' created successfully.")

def view_credentials():
    print(f"\nView stored credentials in {file_name}...\n") 

    # Display the text file contents
    with open(file_name, "r") as file:
        print(rot3_decrypt(file.read()))

def rot3_encrypt(new_record):
    # Provide simple rot3 encryption on all written data and, decryption on read data 
    result = ""

    for char in new_record:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') + 3) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') + 3) % 26) + ord('A'))
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

def rot3_decrypt(encrypted_record):

    #Decrypts text encrypted with the ROT3 cipher.
    result = ""
    for char in encrypted_record:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') - 3 + 26) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') - 3 + 26) % 26) + ord('A'))
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

def menu():
    # Set an initial value for choice other than the value for 'quit'. 
    choice = '' 

    # Start a loop that runs until the user enters the value for 'quit'. 
    while choice != 'q': 
        # Give all the choices in a series of print statements. 
        print("\n[1] Add stored credentials (username, password and URL/resource).") 
        print("[2] View stored credentials.") 
        print("[q] Enter q to quit.")  

        # Ask for the user's choice. 
        choice = input("\nMake your choice ") 

        # Respond to the user's choice. 
        if choice == '1': 
            store_credentials()
        elif choice == '2': 
            view_credentials()
        elif choice.lower() == 'q': 
            print("\nExiting the program...\n") 
        else: 
            print("\nInvalid option, please try again.\n") 

menu()