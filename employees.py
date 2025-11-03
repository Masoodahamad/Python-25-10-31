employees = []

def add_employee(employee):
    employees.append(employee)
    print("Employee added successfully")

def search_employee(id):
    i = 0
    for employee in employees:
        if employee["id"] == id:
            return i
        i += 1
    return -1

def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employees[index]["salary"] = salary
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

add_employee({"id" : 1 , "name" : "Masood", "role" : "Software Engineer" , "salary" : 50000})
add_employee({"id" : 2, "name" : "raju", "role" : "Data Analyst", "salary" : 40000})
add_employee({"id" : 3, "name" : "sajib", "role" : "Backend Engineer", "salary" : 45000})
add_employee({"id" : 4, "name" : "ramu", "role" : "Frontend Engineer", "salary" : 35000})

print(employees)

update_employee(4, 40000)
delete_employee(3)
index = search_employee(1)
if index != -1:
    print("Searched employee :" , employees[index])
else:
    print("Employee not found")

print(employees)