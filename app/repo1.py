
employees = []

def add_employee(employee):
    employees.append(employee)
    print(f"Employee added successfully")

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
    else:
        print("Employee not found")


def delete_employee(id):
    index = search_employee(id)
    if index != -1:
        employees.pop(index)
        print("Employee deleted successfully")
    else:
        print("Employee not found")

