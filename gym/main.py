
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
    
