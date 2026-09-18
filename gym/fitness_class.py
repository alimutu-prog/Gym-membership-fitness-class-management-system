# Represents a fitness class offered by the gym.
class FitnessClass:

    # Initialize a new fitness class with its basic information.
    def __init__(self, class_id, class_name, instructor, schedule, capacity):
        self.class_id = class_id
        self.class_name = class_name
        self.instructor = instructor
        self.schedule = schedule
        self.capacity = capacity
        self.registered_count = 0

    # Check whether the class has reached its maximum capacity.
    def is_full(self):
        return self.registered_count >= self.capacity

    # Increase the number of registered members by one.
    def add_registration(self):
        self.registered_count += 1

    # Decrease the number of registered members when someone cancels.
    def remove_registration(self):
        if self.registered_count > 0:
            self.registered_count -= 1

    # Display all important details about the fitness class.
    def display_details(self):
        status = "FULL" if self.is_full() else "OPEN"

        print(
            f"ID: {self.class_id} | "
            f"Name: {self.class_name} | "
            f"Instructor: {self.instructor} | "
            f"Schedule: {self.schedule} | "
            f"Capacity: {self.registered_count}/{self.capacity} | "
            f"Status: {status}"
        )

    # Convert the fitness class information into a CSV row.
    def to_row(self):
        return [
            self.class_id,
            self.class_name,
            self.instructor,
            self.schedule,
            str(self.capacity),
            str(self.registered_count)
        ]

    # Recreate a FitnessClass object from a CSV row.
    @staticmethod
    def from_row(row):

        # Extract the values from the CSV row.
        class_id, class_name, instructor, schedule, capacity, registered_count = row

        # Create a fitness class using the saved information.
        fitness_class = FitnessClass(
            class_id,
            class_name,
            instructor,
            schedule,
            int(capacity)
        )

        # Restore the number of currently registered members.
        fitness_class.registered_count = int(registered_count)

        return fitness_class
