class Employee:
    def __init__(self,id,name,Salary):
     self.id=id
     self.name=name
     self.Salary=Salary

    def display_info(self):
        print("ID is:",self.id)
        print("Name is:",self.name)
        print("Salary is:",self.Salary)

    def annual_salary(self):
       ann_salary=self.Salary*12
       print(ann_salary)

class Manager(Employee):
    def __init__(self,id,name,Salary,department):
     super().__init__(id,name,Salary)
     self.department=department

    def display_info(self):
        print("ID is:",self.id)
        print("Name is:",self.name)
        print("Salary is:",self.Salary)
        print("Department is:",self.department)

emp1=Employee(1,"Faiqa",150000)
Manager1=Manager(2,"Anas",250000,"IT")

print("Employee Information")
emp1.display_info()
emp1.annual_salary()
print("Manager Information")
Manager1.display_info()
Manager1.annual_salary()




    
   
   

