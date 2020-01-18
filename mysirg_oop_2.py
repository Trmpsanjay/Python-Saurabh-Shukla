class Employee:
    def __init__(self):
        self.empid=int(input("Enter employee id "))
        self.name=input("enter name ")
        self.salary=int(input("enter salary "))
    def display(self):
        print("Name: ",self.name,"\n Emp Id : ",self.empid," \n salary:",self.salary)

Empl=Employee()
Empl.display()
