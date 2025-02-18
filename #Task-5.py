class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Raise of ${amount:.2f} given. New salary is ${self.salary:.2f}.")
        else:
            print("Raise amount must be positive.")
    def display_employee(self):
        print(f"Employee Details:\nName: {self.name}\nPosition: {self.position}\nSalary: ${self.salary:.2f}")

employee = Employee("ADRIAN DELOS SANTOS", "PRESIDENT OF SOFTWARE DEVELOPMENT COMPANY", 125000)

employee.give_raise(500000)

employee.display_employee()