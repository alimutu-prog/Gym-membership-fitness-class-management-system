#this file handles  read and write for the system
#uses simple CSV files stored in the data folder
#survives open and closure of the program

#Files used 
 #mebers.csv,classes.csv,registrations.csv;all one row per paramater


import csv 
import os

from member import Member
from fitness_class import FitnessClass
from registrtion import Registrtion

DATA_FOLDER = "data"
MEMBERS_FILE = os.path.join(DATA_FOLDER, "members.csv")
CLASSES_FILE = os.path.join(DATA_FOLDER, "classes.csv")
REGISTRATIONS_FILE = os.path.join(DATA_FOLDER, "registrations.csv")


def ensure_data_folder():
    #Create the data folder if it does not already exist.

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

# SECTION 1: MEMBERS  

def save_members(members):
    #Write the full list of Member objects to members.csv.

    ensure_data_folder()
    with open(MEMBERS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for member in members:
            writer.writerow(member.to_row())


def load_members():
    #Read members.csv and return a list of Member objects.
    #If the file does not exist yet (e.g. first time the program runs),
    #this is not treated as a crash -- we simply start with an empty list.

    members = []
    try:
        with open(MEMBERS_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:  # skip any blank lines
                    members.append(Member.from_row(row))
    except FileNotFoundError:
        print("[Info] No existing members file found. Starting fresh.")
    return members

# SECTION 2: CLASSES

def save_classes(classes):
    #Write the full list of FitnessClass objects to classes.csv.

    ensure_data_folder()
    with open(CLASSES_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for fitness_class in classes:
            writer.writerow(fitness_class.to_row())


def load_classes():
    #Read classes.csv and return a list of FitnessClass objects.

    classes = []
    try:
        with open(CLASSES_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    classes.append(FitnessClass.from_row(row))
    except FileNotFoundError:
        print("[Info] No existing classes file found. Starting fresh.")
    return classes

# SECTION 3: REGISTRATIONS

def save_registrations(registrations):
    #Write the full list of Registration objects to registrations.csv.

    ensure_data_folder()
    with open(REGISTRATIONS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for registration in registrations:
            writer.writerow(registration.to_row())


def load_registrations():
    #Read registrations.csv and return a list of Registration objects.

    registrations = []
    try:
        with open(REGISTRATIONS_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    registrations.append(Registration.from_row(row))
    except FileNotFoundError:
        print("[Info] No existing registrations file found. Starting fresh.")
    return registrations

# SECTION 4: SAVE/LOAD ALL

def save_all(gym_system):
    #Save members, classes, and registrations in one call.

    save_members(gym_system.members)
    save_classes(gym_system.classes)
    save_registrations(gym_system.registrations)


def load_all():
    #Load members, classes, and registrations in one call.
    #Returns a tuple: (members, classes, registrations)

    return load_members(), load_classes(), load_registrations()