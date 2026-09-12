"""
Contains the FitnessClass class, which represents one fitness class
(e.g. Yoga, Spin, Zumba) offered by the gym.
"""


class FitnessClass:
    """Represents a single fitness class offered by the gym."""

    def __init__(self, class_id, class_name, instructor, schedule, capacity):
        self.class_id = class_id            # str, unique e.g. "C001"
        self.class_name = class_name        # str e.g. "Yoga"
        self.instructor = instructor        # str
        self.schedule = schedule            # str e.g. "Mon 6:00 PM"
        self.capacity = capacity            # int, max number of members
        self.registered_count = 0           # int, how many are registered now
        # Starts at 0 for every new class, since nobody is registered yet
        # at the moment the class is created.

    def is_full(self):
        """Return True if the class has reached its maximum capacity."""
        return self.registered_count >= self.capacity
        # >= (not ==) is used so this stays correct even in the unlikely
        # case registered_count somehow ends up above capacity.

    def add_registration(self):
        """Increase the registered count by one (called when someone joins)."""
        self.registered_count += 1
        # This method only tracks the *count* — the actual link between a
        # specific Member and this class is expected to be stored separately,
        # in a Registration object.

    def remove_registration(self):
        """Decrease the registered count by one (called when someone cancels)."""
        if self.registered_count > 0:
            self.registered_count -= 1
            # The guard above prevents registered_count from ever going
            # negative if this is called more times than add_registration was.

    def display_details(self):
        """Print this class's details, including how full it is."""
        status = "FULL" if self.is_full() else "OPEN"
        # status is computed fresh each time this runs, so it always
        # reflects the current registered_count, not a stored/stale value.
        print(f"ID: {self.class_id} | Name: {self.class_name} | "
              f"Instructor: {self.instructor} | Schedule: {self.schedule} | "
              f"Capacity: {self.registered_count}/{self.capacity} | Status: {status}")

    def to_row(self):
        """Convert this class into a list of strings for saving to CSV."""
        return [self.class_id, self.class_name, self.instructor, self.schedule,
                str(self.capacity), str(self.registered_count)]
        # capacity and registered_count are explicitly converted to str
        # here, since CSV rows are lists of strings, not mixed types.

    @staticmethod
    def from_row(row):
        """Rebuild a FitnessClass object from a CSV row (list of strings)."""
        class_id, class_name, instructor, schedule, capacity, registered_count = row
        # Unpacking: row must have exactly 6 items, in this exact order,
        # matching what to_row() produced above.
        fc = FitnessClass(class_id, class_name, instructor, schedule, int(capacity))
        # capacity is converted back to int here, since __init__ expects
        # a number, not the string that was read from the CSV file.
        fc.registered_count = int(registered_count)
        # registered_count is set directly after creation, since __init__
        # always starts a fresh class at 0 — this overwrites that default
        # with the real saved value from the file.
        return fc

