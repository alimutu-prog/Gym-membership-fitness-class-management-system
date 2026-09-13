class GymSystem:
    def __init__(self):
        self.members=[]
        self.classes=[]
        self.registrations=[]
        
   #This function autogenerates the member ID  
    def generate_member_id(self):
        return f"M{len(self.members) + 1:03d}"