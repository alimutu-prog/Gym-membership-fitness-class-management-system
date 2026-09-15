
# Importing the Gymsystem class from the gym_system module
from gym_system import Gymsystem

# This function asks the user to enter a value that cannot be empty
def get_nonempty_string(prompt):

 # Keep asking until the user enters something
    while True:

# Display the prompt and remove extra spaces        
        value=input(prompt).strip()

  # Check if the user entered nothing
        if value=="":
            print("This field cannot be empty.Please make another attempt")
        else:

 # Return the value if it is not empty
            return value

# This function gets a valid whole number from the user
# min_value can be used to set the smallest allowed number
def get_valid_int(prompt,min_value=None):

  # Keep asking until the user enters a valid number
    while True:
# Get the user's input
     
        raw_value=input(prompt)
        try:
 # Convert the input from a string to an integer
            value=int(raw_value)
        except ValueError:

# This happens when the user enters something
# that cannot be converted into a whole number
            print("invalid input.Please enter a whole number(eg.33)")
            continue

# Check whether a minimum value was provided
# and whether the entered number is too small
        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.Pleae make another attempt")
        return value

# This function gets a choice from a menu
# valid_choices contains the choices that are allowed
def get_menu_choice(prompt,valid_choices):

 # Keep asking until the user enters a valid choice
    while True:

        choice=input(prompt).strip()
        if choice in valid_choices:
            return choice

# Display an error message when the choice is invalid
        print("invalid choice.please enter one of:{','.join(valid_choices)}")
    



#Menu actions
```python
def action_add_member(gym):
    # Show the add-member section
    print("\n**** Add New Member ***")

    # Get member details from the user
    name = get_nonempty_string("Enter member name: ")
    age = get_valid_int("Enter member age: ", min_value=1)
    membership_type = get_nonempty_string(
        "Enter membership type (Basic/Premium): "
    )
    contact = get_nonempty_string("Enter contact (phone/email): ")

    try:
        # Add the member to the system
        new_member = gym.add_member(name, age, membership_type, contact)

        # Show the new member ID
        print(f"Member added successfully with ID: {new_member.member_id}")

    except ValueError as e:
        # Show validation errors
        print(f"Could not add member: {e}")


def action_display_members(gym):
    # Display all members
    gym.display_members()


def action_search_member(gym):
    # Show the search section
    print("\n--- Search Member ---")

    # Get the search keyword
    keyword = get_nonempty_string("Enter member ID or name to search: ")

    # Search for matching members
    results = gym.search_member(keyword)

    if not results:
        # No matching members found
        print("No matching members found.")
    else:
        # Display the number of matches
        print(f"\nFound {len(results)} matching member(s):")

        # Display each matching member
        for m in results:
            m.display_details()


def action_add_class(gym):
    # Show the add-class section
    print("\n--- Add Fitness Class ---")

    # Get class details from the user
    class_name = get_nonempty_string("Enter class name (e.g. Yoga): ")
    instructor = get_nonempty_string("Enter instructor name: ")
    schedule = get_nonempty_string(
        "Enter schedule (e.g. Mon 6:00 PM): "
    )
    capacity = get_valid_int("Enter class capacity: ", min_value=1)

    try:
        # Add the class to the system
        new_class = gym.add_class(
            class_name, instructor, schedule, capacity
        )

        # Show the new class ID
        print(f"Class added successfully with ID: {new_class.class_id}")

    except ValueError as e:
        # Show validation errors
        print(f"Could not add class: {e}")


def action_display_classes(gym):
    # Display all fitness classes
    gym.display_classes()


def action_register_for_class(gym):
    # Show the registration section
    print("\n--- Register Member for Class ---")

    # Get member and class IDs
    member_id = get_nonempty_string("Enter member ID: ")
    class_id = get_nonempty_string("Enter class ID: ")

    try:
        # Register the member for the class
        new_registration = gym.register_for_class(
            member_id, class_id
        )

        # Show the registration ID
        print(
            f"Registration successful! "
            f"Registration ID: {new_registration.registration_id}"
        )

    except ValueError as e:
        # Show registration errors
        print(f"Registration failed: {e}")


def action_cancel_registration(gym):
    # Show the cancellation section
    print("\n--- Cancel Registration ---")

    # Get the registration ID
    registration_id = get_nonempty_string(
        "Enter registration ID to cancel: "
    )

    try:
        # Cancel the registration
        cancelled = gym.cancel_registration(registration_id)

        # Confirm the cancellation
        print(
            f"Registration {cancelled.registration_id} "
            f"has been cancelled."
        )

    except ValueError as e:
        # Show cancellation errors
        print(f"Could not cancel registration: {e}")


def action_view_member_registrations(gym):
    # Show the member registrations section
    print("\n--- View a Member's Classes ---")

    # Get the member ID
    member_id = get_nonempty_string("Enter member ID: ")

    # Display the member's registrations
    gym.display_registrations_for_member(member_id)


def action_view_all_registrations(gym):
    # Display all registrations
    gym.display_all_registrations()


def action_save(gym):
    try:
        # Save the current gym data
        gym.save_data()

    except OSError as e:
        # Handle saving errors
        print(f"Something went wrong while saving data: {e}")
```


MENU_TEXT = """ 
   GYM MANAGEMENT SYSTEM 
1. Add Member 
2. Display All Members 
3. Search Member 
4. Add Fitness Class 
5. Display All Fitness Classes 
6. Register Member for a Class 
7. Cancel a Registration 
8. View a Member's Registered Classes 
9. View All Registrations 
10. Save Data 
11. Exit 
""" 


def main(): 
    # Create the main GymSystem object.
    gym = GymSystem() 
 
    # Load previously saved data when the application starts.
    gym.load_data()

    # Inform the user that saved data has been loaded.
    print("Welcome! Previously saved data (if any) has been loaded.") 
 
    # Create a list of valid menu choices from 1 to 11.
    valid_choices = [str(n) for n in range(1, 12)] 
 
    # Keep showing the menu until the user chooses Exit.
    while True:

        # Display the main menu.
        print(MENU_TEXT)

        # Ask the user for a valid menu choice.
        choice = get_menu_choice(
            "Enter your choice (1-11): ",
            valid_choices
        ) 
 
        # Add a new member.
        if choice == "1": 
            action_add_member(gym) 

        # Display all registered members.
        elif choice == "2": 
            action_display_members(gym) 

        # Search for a specific member.
        elif choice == "3": 
            action_search_member(gym) 

        # Add a new fitness class.
        elif choice == "4": 
            action_add_class(gym) 

        # Display all available fitness classes.
        elif choice == "5": 
            action_display_classes(gym) 

        # Register a member for a fitness class.
        elif choice == "6": 
            action_register_for_class(gym) 

        # Cancel an existing registration.
        elif choice == "7": 
            action_cancel_registration(gym) 

        # Show the classes registered by a specific member.
        elif choice == "8": 
            action_view_member_registrations(gym) 

        # Display all registrations in the system.
        elif choice == "9": 
            action_view_all_registrations(gym) 

        # Save the current gym data.
        elif choice == "10": 
            action_save(gym) 

        # Save data and exit the application.
        elif choice == "11": 

            # Automatically save before exiting so no data is lost.
            action_save(gym)

            # Display a goodbye message.
            print("Data saved. Goodbye!")

            # Stop the menu loop and close the program.
            break 
 
 
# Run main() only when this file is executed directly.
if __name__ == "__main__": 
    main()    
