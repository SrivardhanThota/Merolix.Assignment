class Employee:
    def __init__(self, name, Id, Department, Branch,Gender):
        self.name = name
        self.Id = Id
        self.Department = Department
        self.Branch=Branch
        self.Gender=Gender

Employee1 = Employee("Srivardhan", 999, "Python","Hyderabad","Male" )
Employee2 = Employee("Thota",123,"Java","Hyderabad","Male")
Employee3 = Employee("Raj",111,"python","Hyderabad","Male")
Employee4 = Employee("charan",222,"Networking","Hyderabad","Male")
Employee5 = Employee("Sagar",2345,"Java","Hyderabad","Male")
Employee6 = Employee("Sathish",456,"Python","Hyderabad","Male")
Employee7 = Employee("Poorna",888,"Devops","Hyderabad","Male")
Employee8 = Employee("Harish",789,"Devops","Hyderabad","Male")
Employee9 = Employee("Swamy",889,"Technical Support","Hyderabad","Male")
Employee10 =Employee("Sreenu",999,"Technical Support","Hyderabad","Male")

print("Employee Name:", Employee1.name)
print("Employee Id:", Employee1.Id)
print("Employee Department:", Employee1.Department)
print("Employee Branch:", Employee1.Branch)
print("Employee Gender:", Employee1.Gender)


