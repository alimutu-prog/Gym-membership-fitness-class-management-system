#Gym Membership Fitness
#Registration Desk
#Codes by Vincent Mussa-Registrar
#Creating classes for registration which will have the main details of a member taking part in one of the Gym sessions
#It will include Registartion number, Member number, Session in Gym, Registration date and Status if active or cancelled session,

class Registration:
    def __init__(self, registration_id, member_id, gymclass_id, registration_date, status):
        self.registration_id = registration_id
        self.member_id = member_id
        self.gymclass_id = gymclass_id
        self.registration_date = registration_date
        self.status = status

#Now this will need to be displayed and I will create a method/action that helps to display registration details
    def display_details(self):
        print(f"Registration ID: {self.registration_id}")
        print(f"Member ID: {self.member_id}")
        print(f"Gym Class ID: {self.gymclass_id}")
        print(f"Registration Date: {self.registration_date}")
        print(f"Status: {self.status}")

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
            proint("Member ID is invalid")
            return



