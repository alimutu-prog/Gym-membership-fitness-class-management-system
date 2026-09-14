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