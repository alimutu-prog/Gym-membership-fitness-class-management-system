#This is the registration class which links one Member to one FitnessClass which represents "this member signed up for this class").

import datetime


class Registration:
    #Represents one member's registration for one fitness class.

    def __init__(self, registration_id, member_id, class_id,
                 registration_date=None, status="Active"):
        self.registration_id = registration_id      # str, unique e.g. "R001"
        self.member_id = member_id                  # str, links to Member
        self.class_id = class_id                    # str, links to FitnessClass
        self.registration_date = registration_date or datetime.date.today().isoformat()
        self.status = status                         #Either "Active" or "Cancelled"


def cancel(self):
        """Mark this registration as cancelled."""
        self.status = "Cancelled"

    def display_details(self):
        """Print this registration's details in a readable single line."""
        print(f"Reg ID: {self.registration_id} | Member: {self.member_id} | "
              f"Class: {self.class_id} | Date: {self.registration_date} | "
              f"Status: {self.status}")

def to_row(self):
        """Convert this registration into a list of strings for saving to CSV."""
        return [self.registration_id, self.member_id, self.class_id,
                self.registration_date, self.status]

    @staticmethod
    def from_row(row):
        """Rebuild a Registration object from a CSV row (list of strings)."""
        registration_id, member_id, class_id, registration_date, status = row
        return Registration(registration_id, member_id, class_id,
                             registration_date, status)
