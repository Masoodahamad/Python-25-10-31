import db_json as db
from log import logging
employees = db.read_employees()

def add_employee(employee):
    try:
      employees.append(employee)
      logging.debug(employee)
      db.write_employee(employees)
      logging.info("Employee added successfully")
    except Exception as ex:
        logging.exception(f'Employee added failed {ex}')
        

def search_employee(id):
    i = 0
    for employee in employees:
        if employee.id == id:
            logging.info('Employee Exist')
            return i
        i += 1
    logging.info("Employee doesn't exist")
    return -1

def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employees[index].salary = salary
        db.write_employee(employees)
        logging.info("Employee salary updated")
    else:
        logging.info("Employee not found")


def delete_employee(id):
    index = search_employee(id)
    if index != -1:
        employees.pop(index)
        db.write_employee(employees)
        logging.info("Employee deleted successfully")
    else:
        logging.info("Employee not found")

        