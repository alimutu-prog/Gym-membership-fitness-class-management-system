#This file tests the file-handling part of the Gym Management System.
#It checks that the system can handle missing data and save/load data correctly.
import os
import shutil
import file_handler
from gym_system import Gymsystem

# We check if the data folder already exists.
 # This is important because old test data could affect our results.
if os.path.exists(file_handler.DATA_FOLDER):


# We delete the old data so that the test starts with a clean system.
    shutil.rmtree(file_handler.DATA_FOLDER)

# TC1: Test what happens when the application is run for the first time
 # and no member data exists yet.

members=file_handler.load_members()

# We expect an empty list because no member data exists. 
# # If the list is empty, the test passes. #
#  Otherwise, the test fails.
print("TC1:","PASS" if members==[] else "FAIL")


# TC2: Test whether data can be saved and recovered after restarting 
#the Gym Management System.
gym=Gymsystem()
gym.add_member("Alice Wong",22,"Premium","alice@gmail.com")
gym.add_class("Yoga","Coach Lee","Mon 6PM",5)

# We save the member and class information to the data files. gym.save_data()
gym.save_data()

# We create a completely new GymSystem object.
 # This simulates closing the application and opening it again. reloaded_gym = GymSystem()
reloaded_gym=Gymsystem()
reloaded_gym.load_data()


print("TC2:","PASS" if len(reloaded_gym.members)==1 and len(reloaded_gym.classes)==1 else "FAIL")

# We remove the test data after the tests are finished. 
# This keeps the project clean and prevents test data
#  # from affecting future tests.
shutil.rmtree(file_handler.DATA_FOLDER)