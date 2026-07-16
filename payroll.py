# Employee Payroll System using Class, Constructor and Destructor

class Employee:

    # Constructor
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        print("\nConstructor Called")

    # Calculate Gross Salary
    def calculate_salary(self):
        hra = self.basic_salary * 0.20
        da = self.basic_salary * 0.10
        gross_salary = self.basic_salary + hra + da
        return gross_salary

    # Display Employee Details
    def display(self):
        print("\n------ Employee Details ------")
        print("Employee ID   :", self.emp_id)
        print("Employee Name :", self.name)
        print("Basic Salary  :", self.basic_salary)
        print("Gross Salary  :", self.calculate_salary())

    # Destructor
    def __del__(self):
        print("\nDestructor Called")
        print("Employee Object Deleted")


# Main Program
emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

emp = Employee(emp_id, name, basic_salary)
emp.display()

del emp           # Delete object