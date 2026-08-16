from pydantic import BaseModel


# Creating Model/Class
class Employee(BaseModel):
    id: int
    name: str
    salary: float
    department: str


# Function to add employee
def add_employee(employee: Employee):
    print(f"Employee {employee.name} added")


# Function to display employee details
def display_employee(employee: Employee):
    print("----- Employee Details -----")
    print(f"ID: {employee.id}")
    print(f"Name: {employee.name}")
    print(f"Salary: {employee.salary}")
    print(f"Department: {employee.department}")


# Function to calculate bonus
def calculate_bonus(employee: Employee):
    bonus = employee.salary * 0.10
    print(f"Bonus: {bonus}")


# Dictionary data
employee_data = {
    "id": 1,
    "name": "Ashmit",
    "salary": 50000,
    "department": "AI"
}


# Creating Object from dictionary
employee_1 = Employee(**employee_data)


# Passing object to functions
add_employee(employee_1)

display_employee(employee_1)

calculate_bonus(employee_1)