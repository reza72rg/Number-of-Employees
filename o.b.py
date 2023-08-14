class Employee:
    def __init__(self, name, age):
        """
        Initialize an Employee object with a name and age.
        """
        self.name = name
        self.age = age

num_employees = int(input("Enter number of employees: "))

# Create a list of Employee objects using a list comprehension
employees = [Employee(input("Enter name of employee {}: ".format(i+1)), input("Enter age of employee {}: ".format(i+1))) for i in range(num_employees)]

# Print the name and age of each employee
for employee in employees:
    print("{} is {} years old".format(employee.name, employee.age))
