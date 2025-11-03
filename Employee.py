class Employee:
   def __init__(self, id, name, role, salary):
      self.id = id
      self.name = name
      self.role = role
      self.salary = salary

   def __repr__(self):
       return f"(id = {self.id}, name = {self.name}, role = {self.role}, salary = {self.salary})"

employees = []
def add_employee(employee):
    employees.append(employee)
    print("Employee added successfully")

def search_employee(id):
    i = 0
    for employee in employees:
        if employee.id == id:
            return i
        i += 1
    return -1

def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employees[index].salary = salary
        print("Employee salary updated")
        print(employees[index])
    else:
        print("Employee not found")

def delete_employee(id):
    index = search_employee(id)
    if index != -1:
        employees.pop(index)
        print("Employee deleted successfully")
    else:
        print("Employee not found")
emp1 = Employee(1, "Masood", "Software Engineer", 50000)
emp2 = Employee(2, "raju", "data analyst", 45000)
emp3 = Employee(3, "ramu", "test engineer", 36000)
add_employee(emp1)
add_employee(emp2)
add_employee(emp3)

print(employees)

update_employee(3, 45000)
delete_employee(3)
index = search_employee(1)
if index != -1:
    print("Searched employee :" , employees[index])
else:
    print("Employee not found")

print(employees)