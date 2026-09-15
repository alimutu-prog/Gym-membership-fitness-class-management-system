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
    
