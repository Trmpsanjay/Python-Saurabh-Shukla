
class student:
    def __init__(self):
        self.name=input("name")
        self.roll=int(input("roll"))
        self.sem=input("enter semester")
        self.branch=input("Enter branch")
    def putdata(self):
        print("name =",self.name)
        print("Roll =",self.roll)
        print("Semester: ",self.sem)
        print("Branch :",self.branch)

s=student()
s.putdata()
