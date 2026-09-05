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


