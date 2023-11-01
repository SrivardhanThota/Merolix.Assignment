class Employee:
    def __init__(self, name, Id, Department):
        self.name = name
        self.Id = Id
        self.Department = Department

Employee1 = Employee("Srivardhan", 999, "Python" )
Employee2 = Employee("Thota",123,"Java")
Employee3 = Employee("Raj",111,"python")
Employee4 = Employee("charan",222,"Networking")
Employee5 = Employee("Sagar",2345,"Java")
Employee6 = Employee("Sathish",456,"Python")
Employee7 = Employee("Poorna",888,"Devops")
Employee8 = Employee("Harish",789,"Devops")
Employee9 = Employee("Swamy",889,"Technical Support")
Employee10 = Employee("Sreenu",999,"Technical Support")

print("Employee Name:", Employee1.name)
print("Employee Id:", Employee1.Id)
print("Employee Department:", Employee1.Department)

