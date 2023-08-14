class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

employees = []

num_employees = int(input("Enter number of employees: "))

for i in range(num_employees):
    name = input("Enter name of employee {}: ".format(i+1))
    age = input("Enter age of employee {}: ".format(i+1))
    employee = Employee(name, age)
    employees.append(employee)

for employee in employees:
    print("{} is {} years old".format(employee.name, employee.age))
    
