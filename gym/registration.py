
"""

This file contains the Registration class.
It represents a member signing up for a fitness class.
"""

# We import datetime so we can automatically record
# the date when a registration is created.
import datetime


class Registration:
    # This class represents one registration.
    # It connects one member to one fitness class.

    def __init__(self, registration_id, member_id, class_id,
                 registration_date=None, status="Active"):

        # Stores a unique registration ID so we can
        # identify each registration.
        self.registration_id = registration_id

        # Stores the member ID to know which member
        # made this registration.
        self.member_id = member_id

        # Store the class ID to know which fitness
        # class the member registered for.
        self.class_id = class_id

        # Stores the registration date.
        # If no date is provided, use today's date automatically.
        self.registration_date = registration_date or datetime.date.today().isoformat()

        # Store the current status of the registration.
        # New registrations are Active by default.
        self.status = status


    def cancel(self):
        # This method is used when a member cancels
        # their registration for a fitness class.

        # Change the status instead of deleting the registration.
        # This allows us to keep a record that the registration existed.
        self.status = "Cancelled"


    def display_details(self):
        # This method displays the registration information
        # in an easy-to-read format.

        print(
            f"Reg ID: {self.registration_id} | "   # Show registration ID
            f"Member: {self.member_id} | "         # Show member ID
            f"Class: {self.class_id} | "            # Show class ID
            f"Date: {self.registration_date} | "   # Show registration date
            f"Status: {self.status}"                # Show current status
        )

#In the program there is a chance that a gym user cancels the session , and we wont delete their other details but only the status will change
#Creating an action that changes registration status to cancelled
    def cancel(self):
        self.status = "Cancelled"

#I need to check if registration works perfectly so I will put class for member and all that my friends are doing I will just later delete it
#Class for member
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

#Also class for GymFitness class/session
class FitnessClass:
    def __init__(self, class_id, class_name, capacity):
        self.class_id = class_id
        self.class_name = class_name
        self.capacity = capacity
#So far created is a class wich contains key details of a member in a gymfitness class like the class id, class name like yoga, capacity maximum it can carry maybe we would use 20
        self.registered_count = 0 #Right now number of registered members is 0 if one registers it increases by 1 and if one cancels it decreases by 1

    def is_full(self):
        return self.registered_count >= self.capacity

    def add_registration(self):
        if not self.is_full():
            self.registered_count += 1
            return True
        else:
            return False

    def remove_registration(self): #This removes a registration and leaves one empty space
        if self.registered_count > 0:
            self.registered_count -= 1
            return True
        else:
            return False

#I also need to test how registration works with members and a class
#Creating a simple manager to hold the members, gym classes and registrations
class GymSystem:
    def __init__(self):
        self.members = []
        self.classes = []
        self.registrations = []

#Method will help bring a member in a Fitness class
    def register_for_class(self, member_id, gymclass_id):
#First is checking if member_id exists
        found_member = None
        for member in self.members:
            if member.member_id == member_id:
                found_member = member

        if found_member == None:
            print("Member ID is invalid")
            return

#Checking if gymclass_id exists
        found_class = None
        for gymclass in self.classes:
            if gymclass.class_id == gymclass_id:
                found_class = gymclass

        if found_class == None:
            print("Gym Class ID is invalid")
            return

#There is possibility one cant register if class is full
        if found_class.is_full():
            print("Cannot register, class is full")
            return

#Now i create real regstration to test then next is to meet up for mergingn final tests and see if system works
        new_id = "R" + str(len(self.registrations) + 1)
#I use letter R out of all because all my Registarion ID starts with R
        new_registration = Registration(new_id, member_id, gymclass_id, "11/09/2026", "Active")
        self.registrations.append(new_registration) #This adds a new registration to the list with all registarions
        found_class.add_registration()
#Different from one above this directs the registration to the class and add one member registered out of the whole capacity
        print(f"Your member ID {member_id} has been succesfully added for {found_class.class_name} class")
        return new_registration
#After the registration is aded one receives a message for complete registration

#Testing if registration works
test = GymSystem()
#Adding members to the system
test.members.append(Member("M001", "Allan"))
test.members.append(Member("M002", "Marcel"))
#Adding classes to the system and its member registration
test.classes.append(FitnessClass("C001", "Yoga", 4))
test.register_for_class("M002", "C001")
test.register_for_class("M001", "C001")








    def to_row(self):
        # This method converts the registration into a list.
        # We do this because the list can be saved as one row
        # in a CSV file.

        return [
            self.registration_id,       # Save registration ID
            self.member_id,             # Save member ID
            self.class_id,              # Save class ID
            self.registration_date,     # Save registration date
            self.status                 # Save registration status
        ]


    @staticmethod
    def from_row(row):
        # This method takes a row read from a CSV file
        # and uses it to create a Registration object.

        # Separate the values from the CSV row
        # and assign them to the correct variables.
        registration_id, member_id, class_id, registration_date, status = row

        # Create and return a Registration object
        # using the information that came from the CSV file.
        return Registration(
            registration_id,
            member_id,
            class_id,
            registration_date,
            status
        )

