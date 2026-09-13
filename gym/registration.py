
"""

This file contains the Registration class.
It represents a member signing up for a fitness class.
"""

# We import datetime so we can automatically record
# the date when a registration is created.
import datetime


class Registration:
    # This class represents one registration.
    # It connects one member to one fitness class.

    def __init__(self, registration_id, member_id, class_id,
                 registration_date=None, status="Active"):

        # Stores a unique registration ID so we can
        # identify each registration.
        self.registration_id = registration_id

        # Stores the member ID to know which member
        # made this registration.
        self.member_id = member_id

        # Store the class ID to know which fitness
        # class the member registered for.
        self.class_id = class_id

        # Stores the registration date.
        # If no date is provided, use today's date automatically.
        self.registration_date = registration_date or datetime.date.today().isoformat()

        # Store the current status of the registration.
        # New registrations are Active by default.
        self.status = status


    def cancel(self):
        # This method is used when a member cancels
        # their registration for a fitness class.

        # Change the status instead of deleting the registration.
        # This allows us to keep a record that the registration existed.
        self.status = "Cancelled"


    def display_details(self):
        # This method displays the registration information
        # in an easy-to-read format.

        print(
            f"Reg ID: {self.registration_id} | "   # Show registration ID
            f"Member: {self.member_id} | "         # Show member ID
            f"Class: {self.class_id} | "            # Show class ID
            f"Date: {self.registration_date} | "   # Show registration date
            f"Status: {self.status}"                # Show current status
        )


    def to_row(self):
        # This method converts the registration into a list.
        # We do this because the list can be saved as one row
        # in a CSV file.

        return [
            self.registration_id,       # Save registration ID
            self.member_id,             # Save member ID
            self.class_id,              # Save class ID
            self.registration_date,     # Save registration date
            self.status                 # Save registration status
        ]


    @staticmethod
    def from_row(row):
        # This method takes a row read from a CSV file
        # and uses it to create a Registration object.

        # Separate the values from the CSV row
        # and assign them to the correct variables.
        registration_id, member_id, class_id, registration_date, status = row

        # Create and return a Registration object
        # using the information that came from the CSV file.
        return Registration(
            registration_id,
            member_id,
            class_id,
            registration_date,
            status
        )

