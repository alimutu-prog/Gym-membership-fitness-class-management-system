#this file handles  read and write for the system
#uses simple CSV files stored in the data folder
#survives open and closure of the program

#Files used 
 #mebers.csv,classes.csv,registrations.csv;all one row per paramater


import csv #R&W files
import os #interact with my machine OS


from member import Member
from fitness_class import FitnessClass
from registrtion import Registrtion



#main folder where project data stay
DATA_FOLDER="data"

#initializing safe file paths storage
MEMBERS_FILE=os.path.join(DATA_FOLDER,"members.csv")

CLASSES_FILE=os.path.join(DATA_FOLDER,"classes.csv")

REGISTRATIONS_FILE=os.path.join(DATA_FOLDER,"registrtions.csv")


