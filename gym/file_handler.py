#this file handles  read and write for the system
#uses simple CSV files stored in the data folder
#survives open and closure of the program

#Files used 
 #mebers.csv,classes.csv,registrations.csv;all one row per paramater


import csv #R&W files
import os #interact with my machine OS


from member import Member
from fitness_class import FitnessClass
from registrtion import Registration



#main folder where project data stay
DATA_FOLDER="data"

#initializing safe file paths storage
MEMBERS_FILE=os.path.join(DATA_FOLDER,"members.csv")

CLASSES_FILE=os.path.join(DATA_FOLDER,"classes.csv")

REGISTRATIONS_FILE=os.path.join(DATA_FOLDER,"registrtions.csv")



#checking if teh folder in that path has already being created if not then one gonna be created
def ensure_data_folder():
    """"Create the data folder if it does not exist."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)



                #MEMBERS
def save_members(members):
    """"write the full list of member objects to members.csv."""

    ensure_data_folder()

#open and closes the file safely during write
    with open(MEMBERS_FILE,'w', newline="" , encoding="utf-8") as f:
#file formatter
        writer=csv.writer(f)

#loop throgh members list and arrnge them in rowa
        for member in members:
            writer.writerow(member.to_row())


def load_members():
    "Read members.csv and return full list of meber objects"
    "if the file does not exist yet,its not treated as crash but starting frsh empty list"

    members=[] #will member objects  from file reconstruct 
    try:
        #read only
        with open(MEMBERS_FILE,"r",newline="", encoding="utf-8")as f:
            reader=csv.reader(f)

            for row in reader:

                if row:#skips blanks row

                    members.append(Member.from_row(row))

    except FileNotFoundError:

        print("[info] No existing members file found.start afresh")

    return members

                #CLASSES

def save_classes(classes):
    """Writing the full list of fitness class objects to classes.csv"""
    ensure_data_folder()
    with open(CLASSES_FILE,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        for fitness_class in classes:
            writer.writerow(fitness_class.to_row())


def load_classes():
    """Reads classes.csv and return a list of FitnessClass objects"""
    classes=[]
    try:
        with open(CLASSES_FILE,"r",newline="",encoding="utf-8") as f:
            reader=csv.reader(f)
            for row in reader:
                if row:
                    classes.append(FitnessClass.from_row(row))
    except FileNotFoundError:
        print("[info] No existing classes found.start afresh")
    return classes



                  #REGISTRTIONS
def save_registrations(registrations):

    ensure_data_folder

    with open(REGISTRATIONS_FILE,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        for registrtion in registrations:
            writer.writerow(registrtion.to_row)


def load_registrations():

    registrations=[]
    try:


       with open(REGISTRATIONS_FILE, "r", newline="", encoding="utf-8") as f:
            reader=csv.reader(f)
            for row in reader:
                if row:
                    registrations.append(Registration.from_row(row))
    except FileNotFoundError:
         print("[Info] No existing registrations file found. Starting fresh.")
    return registrations




#SAVING AND LOADING ALL

def save_all(gym_system):

    save_members(gym_system.members)
    save_classes(gym_system.classes)
    save_registrations(gym_system.registartions)

def load_all():

    return load_members,load_classes,load_registrations()
    

