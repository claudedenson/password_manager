import manage_credentials

# Define menu options using a tuple
menu_options_tuple = (
    "Add stored credentials (username, password and URL/resource).", 
    "View stored credentials.", 
    "Select 3 to quit."
    )

# Displays the menu options to the user.
def display_menu(menu_options):
    print("\n==== Simple Password Manager ====\n") 

    for i, option in enumerate(menu_options):
        print(f"[{i + 1}]. {option}")

    print("\n-----------------------------------")

# Prompts the user for their choice and validates the input.
def get_choice(menu_options):
    while True:
        try:
            choice = int(input("\nMake your choice: "))
            if 1 <= choice <= len(menu_options):
                return choice
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def menu():
    # Set an initial value for choice other than the value for 'quit'. 
    choice = '' 

    # Start a loop that runs until the user enters the value for 'quit'. 
    while choice != 'q': 
        # Give all the choices in a series of print statements. 
        # print("\n[1] Add stored credentials (username, password and URL/resource).") 
        # print("[2] View stored credentials.") 
        # print("[q] Enter q to quit.")  

        display_menu(menu_options_tuple)

        # Ask for the user's choice. 
        choice = get_choice(menu_options_tuple)

        # Respond to the user's choice. 
        if choice == 1: 
            manage_credentials.store_credentials()
        elif choice == 2: 
            manage_credentials.view_credentials()
        elif choice == 3: 
            print("\nExiting the program...\n") 
            break
        else: 
            print("\nInvalid option, please try again.\n") 

# Executes the main program
menu()