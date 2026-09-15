from member import Member

class GymSystem:
    def __init__(self):
        self.members=[]
        self.classes=[]
        self.registrations=[]

   #This function autogenerates the member ID  
    def generate_member_id(self):
        return f"M{len(self.members) + 1:03d}"

    # This function creates a new member and adds it to the system.
    # It returns a new member object.
    # Raises a ValueError if a duplicate name and contact exist. 
    def add_member(self,name,age,membership_type,contact):
        for m in self.members:
            if m.contact==contact:
                raise ValueError(f"A member with contact {contact} already exists.")
        member_id=self.generate_member_id()
        new_member=Member(member_id,name,age,membership_type,contact)
        self.members.append(new_member)
        return new_member

    # This function prints every registered member and handles the case where there are no registered members yet.
    def display_members(self):
        if not self.members:
            print("No members registered yet.")
            return
        print('\n--- Registered Members ---')
        for m in self.members:
            m.display_details()

    # This function searches members by ID or name(case-insensitive,partial match )
    # It returns a list of matching Member objects(maybe empty).
    def search_member(self,keyword):
        keyword=keyword.lower().strip()
        results=[
            m for m in self.members
            if keyword in m.member_id.lower() or keyword in m.name.lower()
        ]
        return results

#    This function returns the Member with this exact ID, or None if not found.
    def find_member_by_id(self,member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None
    

#Fitness class management

    def generate_class_id(self):

        #Create the next class ID, e.g. C001, C002, ...
        return f"C{len(self.classes) + 1:03d}"

    def add_class(self, class_name, instructor, schedule, capacity):

        #Create a new FitnessClass and add it to the system.
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        class_id = self.generate_class_id()
        new_class = FitnessClass(class_id, class_name, instructor, schedule, capacity)
        self.classes.append(new_class)
        return new_class

    def display_classes(self):

        #Print every fitness class currently offered.
        if not self.classes:
            print("No fitness classes have been added yet.")
            return
        print("\n--- Fitness Classes ---")
        for c in self.classes:
            c.display_details()

    def find_class_by_id(self, class_id):

        #Return the FitnessClass with this exact ID, or None if not found.
        for c in self.classes:
            if c.class_id == class_id:
                return c
        return None