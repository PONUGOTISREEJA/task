# class Employee:
#     def __init__(self):
#         self.name = "ram"
#         self.id =123
#         self.domain = "python"
#         print(self.name)
#     def display(self):
#         self.salary = 100000
#         print(self.name)
# e = Employee()
# e.display()
# print(e.domain)
# print(e.salary)
# e.company = "marolix"
# print(e.company)

# class Employee:
#     company = "marolix"
#     def __init__(self):
#         Employee.name ="sreeja"
#         Employee.surname ="ponugoti"
#     def m1(self):
#         Employee.id = 12345
#     @classmethod
#     def m2(cls):
#         Employee.salary = 200000
#         cls.domain = "python"
#     @staticmethod
#     def m3():
#         Employee.experience = "3 years"
# e = Employee()
# Employee.city = "hyderabad"
# print(Employee.__dict__)
# e.m1()
# e.m2()
# e.m3()

class Employee :
    company= "marolix"
    def __init__(self):
        Employee.company = "tech mahendra"
        print("in-constructer -",self.company)
    
    @classmethod
    def m2(cls):
        cls.company = "TCS"
        print("inside classmethod using cls -",cls.company)
        print("inside classmethod using classname -",Employee.company)
    @staticmethod
    def m3():
        Employee.company = "HCL"
        print("inside staticmethod using classname -",Employee.company)
    
    
e =Employee()
e.m2()
e.m3()
Employee.company = "infosys"
print("outside of class using classname -",Employee.company)
print("outside of class using Orv -",e.company)


class local:
    def Employee(self):
        name = "sreeja"
        print(name)
l=local()
l.Employee()
