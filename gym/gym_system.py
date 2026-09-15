#The GymSystem class holds the three lists (members, classes, registrations)
#and all the business logic methods that main.py's menu calls into.



# importing the classes and the file handler for data

from member import Member
from fitness_class import FitnessClass
from registration import Registration
import file_handler

#"Initializes the central Gym Management System.
        
# Attributes:
#members (list): Stores all registered Member objects.
#classes (list): Stores all available FitnessClass objects.
# #registrations (list): Stores Registration objects linking members to classes.
#""""



class Gymsystem:
    def __init__(self):
            self.members = []
            self.classes = []
            self.registrations = []




#Registration
def generate_registration_id(self):
    """Create the next registration ID, e.g. R001, R002, ..."""
    # Generate a unique registration ID
    return f"R{len(self.registrations) + 1:03d}"


def register_for_class(self, member_id, class_id):
    """Register a member for a fitness class."""

    # Check if the member exists
    member = self.find_member_by_id(member_id)
    if member is None:
        raise ValueError(f"No member found with ID '{member_id}'.")

    # Check if the class exists
    fitness_class = self.find_class_by_id(class_id)
    if fitness_class is None:
        raise ValueError(f"No class found with ID '{class_id}'.")

    # Check if the class is full
    if fitness_class.is_full():
        raise ValueError(f"Class '{fitness_class.class_name}' is full.")

    # Prevent duplicate active registrations
    for r in self.registrations:
        if (r.member_id == member_id and r.class_id == class_id
                and r.status == "Active"):
            raise ValueError("This member is already registered for this class.")

    # Create and save the new registration
    registration_id = self.generate_registration_id()
    new_registration = Registration(registration_id, member_id, class_id)
    self.registrations.append(new_registration)

    # Update the class's registration count
    fitness_class.add_registration()

    return new_registration


def cancel_registration(self, registration_id):
    """Cancel an existing active registration."""

    # Find the registration by ID
    for r in self.registrations:
        if r.registration_id == registration_id:

            # Prevent cancelling twice
            if r.status == "Cancelled":
                raise ValueError("This registration is already cancelled.")

            # Cancel the registration
            r.cancel()

            # Free up a place in the class
            fitness_class = self.find_class_by_id(r.class_id)
            if fitness_class is not None:
                fitness_class.remove_registration()

            return r

    # Registration ID was not found
    raise ValueError(f"No registration found with ID '{registration_id}'.")


def display_registrations_for_member(self, member_id):
    """Print all classes a given member is registered for."""

    # Find registrations belonging to the member
    matches = [r for r in self.registrations if r.member_id == member_id]

    # Handle members with no registrations
    if not matches:
        print(f"No registrations found for member '{member_id}'.")
        return

    print(f"\n--- Registrations for {member_id} ---")

    # Display each registration
    for r in matches:
        r.display_details()


def display_all_registrations(self):
    """Print every registration in the system."""

    # Check if there are no registrations
    if not self.registrations:
        print("No registrations yet.")
        return

    print("\n--- All Registrations ---")

    # Display every registration
    for r in self.registrations:
        r.display_details()

from member import Member

class GymSystem:
    def __init__(self):
        self.members=[]
        self.classes=[]
        self.registrations=[]

   #This function autogenerates the member ID  
    def generate_member_id(self):
        return f"M{len(self.members) + 1:03d}"

    # This function creates a new member and adds it to the system.
    # It returns a new member object.
    # Raises a ValueError if a duplicate name and contact exist. 
    def add_member(self,name,age,membership_type,contact):
        for m in self.members:
            if m.contact==contact:
                raise ValueError(f"A member with contact {contact} already exists.")
        member_id=self.generate_member_id()
        new_member=Member(member_id,name,age,membership_type,contact)
        self.members.append(new_member)
        return new_member

    # This function prints every registered member and handles the case where there are no registered members yet.
    def display_members(self):
        if not self.members:
            print("No members registered yet.")
            return
        print('\n--- Registered Members ---')
        for m in self.members:
            m.display_details()

    # This function searches members by ID or name(case-insensitive,partial match )
    # It returns a list of matching Member objects(maybe empty).
    def search_member(self,keyword):
        keyword=keyword.lower().strip()
        results=[
            m for m in self.members
            if keyword in m.member_id.lower() or keyword in m.name.lower()
        ]
        return results

#    This function returns the Member with this exact ID, or None if not found.
    def find_member_by_id(self,member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None
    

#Fitness class management

    def generate_class_id(self):

        #Create the next class ID, e.g. C001, C002, ...
        return f"C{len(self.classes) + 1:03d}"

    def add_class(self, class_name, instructor, schedule, capacity):

        #Create a new FitnessClass and add it to the system.
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        class_id = self.generate_class_id()
        new_class = FitnessClass(class_id, class_name, instructor, schedule, capacity)
        self.classes.append(new_class)
        return new_class

    def display_classes(self):

        #Print every fitness class currently offered.
        if not self.classes:
            print("No fitness classes have been added yet.")
            return
        print("\n--- Fitness Classes ---")
        for c in self.classes:
            c.display_details()

    def find_class_by_id(self, class_id):

        #Return the FitnessClass with this exact ID, or None if not found.
        for c in self.classes:
            if c.class_id == class_id:
                return c
        return None
