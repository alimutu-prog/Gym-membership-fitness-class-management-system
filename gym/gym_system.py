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