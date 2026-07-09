class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def calculate_bonus(self):
        return self.salary * 0.10
    
emp1=Employee("John",80000)
emp2=Employee("Mary",95000)

print(emp1.calculate_bonus())
print(emp2.calculate_bonus())
