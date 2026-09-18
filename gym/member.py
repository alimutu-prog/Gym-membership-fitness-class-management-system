
#Creating a class member where we get the member's details 
class Member:

    #This records the member's details
    def __init__(self,member_id,name,age,membership_type,contact):
        self.member_id=member_id
        self.name=name
        self.age=age
        self.membership_type=membership_type
        self.contact=contact

    #This prints the member's details
    def display_details(self):
        print(f"ID: {self.member_id} | Name: {self.name} | Age: {self.age} |"
              f"Membership:{self.membership_type} | Contact: {self.contact} ")
        
    # This takes the member's details and record them as a list of strings. This would be later saved to a csv file. 
    def to_row(self):
        return[self.member_id,self.name,str(self.age),self.membership_type,self.contact]
    
    @staticmethod
    # This rebuilds a Member object from a csv row(which is the list of strings we created )
    def from_row(row):
        member_id,name,age,membership_type,contact=row
        return Member(member_id,name,int(age),membership_type,contact)
    
    



