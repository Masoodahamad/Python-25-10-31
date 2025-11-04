from db_setup import session, Employee

def read_all_employees():
    employees = session.query(Employee).all()
    return employees

def add_employee(employee):
      session.add(employee)
      session.commit()
      print("Employee added successfully")

def search_employee(id, salary):
    employee = session.query(Employee).filter_by(id = id).first()
    return employee


def update_employee(id, salary):
    old_employee = search_employee(id)
    if old_employee:
        old_employee.salary = salary
        session.commit()
        print("Employee updated successfully")
    else:
        print("Employee not found")

def delete_employee(id):
    old_employee = search_employee
    if not old_employee:
        print("Employee NOt Found")
        return
        
    session.delete(old_employee)
    session.commit()
    print("Employee deleted successfully")

        