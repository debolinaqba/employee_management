from employee import Employee

employees = []


def add_employee():

    try:

        emp_id = int(input("Employee ID : "))
        name = input("Name : ")
        age = int(input("Age : "))
        department = input("Department : ")
        salary = float(input("Salary : "))

        emp = Employee(emp_id, name, age, department, salary)

        employees.append(emp)

        print("Employee Added Successfully.")

    except ValueError:

        print("Invalid Input.")



def display_all():

    if len(employees) == 0:

        print("No Employee Found")

    else:

        for emp in employees:

            emp.display()




def search_employee():

    search = int(input("Enter Employee ID : "))

    for emp in employees:

        if emp.emp_id == search:

            emp.display()

            return

    print("Employee Not Found")




def delete_employee():

    search = int(input("Enter Employee ID : "))

    for emp in employees:

        if emp.emp_id == search:

            employees.remove(emp)

            print("Deleted")

            return

    print("Employee Not Found")