#this file handles  read and write for the system
#uses simple CSV files stored in the data folder
#survives open and closure of the program

#Files used 
 #mebers.csv,classes.csv,registrations.csv;all one row per paramater


import csv #R&W files
import os #interact with my machine OS


from member import Member
from fitness_class import FitnessClass
from registration import Registration



#main folder where project data stay
DATA_FOLDER="data"

#initializing safe file paths storage
MEMBERS_FILE=os.path.join(DATA_FOLDER,"members.csv")

CLASSES_FILE=os.path.join(DATA_FOLDER,"classes.csv")

REGISTRATIONS_FILE = os.path.join(DATA_FOLDER, "registrations.csv")



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
            #to_row() turns one Member object into a plain list of strings
            #(e.g. [member_id, name, age, membership_type, contact]) so
            #csv.writer can write it as one line in the file
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

                    #from_row() does the opposite of to_row(): it takes one
                    #raw CSV row (a list of strings) and rebuilds a real
                    #Member object, converting things like age back to int
                    members.append(Member.from_row(row))

    except FileNotFoundError:

        #this is the very first run case, i.e nobody has saved yet -
        #instead of crashing the whole program we just print a friendly
        #note and carry on with an empty list
        print("[info] No existing members file found.start afresh")

    return members

                #CLASSES

def save_classes(classes):
    """Writing the full list of fitness class objects to classes.csv"""
    ensure_data_folder()
    with open(CLASSES_FILE,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        for fitness_class in classes:
            #same idea as save_members: convert each FitnessClass object
            #to a row of strings before writing it to disk
            writer.writerow(fitness_class.to_row())


def load_classes():
    """Reads classes.csv and return a list of FitnessClass objects"""
    classes=[]
    try:
        with open(CLASSES_FILE,"r",newline="",encoding="utf-8") as f:
            reader=csv.reader(f)
            for row in reader:
                if row:
                    #rebuild a real FitnessClass object (including turning
                    #capacity/registered_count back into ints) from the row
                    classes.append(FitnessClass.from_row(row))
    except FileNotFoundError:
        #same first-run situation as load_members() above, just for classes
        print("[info] No existing classes found.start afresh")
    return classes



                  #REGISTRTIONS
def save_registrations(registrations):
    #make sure the data folder actually exists before we try to write into it
    ensure_data_folder()

    #open the registrations file fresh for writing (this replaces whatever
    #was there before with the current, full list of registrations)
    with open(REGISTRATIONS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for registration in registrations:
            #convert each Registration object (id, member_id, class_id,
            #date, status) into one CSV row and write it
            writer.writerow(registration.to_row())


def load_registrations():
    #this will hold every Registration object we manage to read back in
    registrations=[]
    try:

        #open the file for reading only - if it doesn't exist yet this
        #line is what throws FileNotFoundError, caught below
       with open(REGISTRATIONS_FILE, "r", newline="", encoding="utf-8") as f:
            reader=csv.reader(f)
            for row in reader:
                if row: #ignore any accidental blank lines in the file
                    #rebuild a real Registration object from the raw row
                    registrations.append(Registration.from_row(row))
    except FileNotFoundError:
         #first run for registrations specifically - no crash, just start empty
         print("[Info] No existing registrations file found. Starting fresh.")
    return registrations




#SAVING AND LOADING ALL
# SAVING AND LOADING ALL

def save_all(gym_system):
    #convenience function so the rest of the app (main.py / gym_system.py)
    #can save everything in one call instead of calling all three
    #save_ functions separately every time
    save_members(gym_system.members)
    save_classes(gym_system.classes)
    save_registrations(gym_system.registrations)


def load_all():
    #same idea as save_all() but for loading - calls all three load_
    #functions and hands back all three lists together as one tuple, so
    #GymSystem can unpack them in one line when the app starts up
    return load_members(), load_classes(), load_registrations()