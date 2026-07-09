class Employee:

    def __init__(self, emp_id, name, age, department, salary):

        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def annual_salary(self):

        return self.salary * 12

    def display(self):

        print("------------------------------")
        print(f"ID         : {self.emp_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Department : {self.department}")
        print(f"Salary     : {self.salary}")
        print(f"Annual     : {self.annual_salary()}")