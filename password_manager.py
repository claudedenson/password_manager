import manage_credentials

# Give the user some context. 
print("\n==== Simple Password Manager ====") 

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
            manage_credentials.store_credentials()
        elif choice == '2': 
            manage_credentials.view_credentials()
        elif choice.lower() == 'q': 
            print("\nExiting the program...\n") 
        else: 
            print("\nInvalid option, please try again.\n") 

# Executes the main program
menu()