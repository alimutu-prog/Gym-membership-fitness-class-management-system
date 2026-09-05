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