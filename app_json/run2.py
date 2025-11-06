from employee12 import Employee
import repo2
while True:
  print("1 - Add Employee")
  print("2 - Search Employee")
  print("3 - Update Employee")
  print("4 - Delete Employee")
  print("5 - Print All Employee")
  print("6 - Exit")
  choice = int(input())
  if choice == 1:
    print("Enter Id")
    id = int(input())
    print("Enter Name")
    name = input()
    print("Enter Job title")
    title = input()
    print("Enter Salary:")
    salary = input()
    repo2.add_employee(Employee(id=id, name=name, job_title=title, salary=salary))
  elif choice == 2:
    print("Enter id to search:")
    id = int(input())
    old_employee = repo2.search_employee(id)
    if not old_employee:
       print("Employee not found")
    else:
       print("Searched Employee: ", old_employee)

        
  elif choice == 3:
    print("Enter id to update")
    id = int(input())
    print("Enter salary to update")
    salary = int(input())
    repo2.update_employee(id, salary)
  elif choice == 4:
    print("Enter id to delete")
    id = int(input())
    old_employee = repo2.search_employee(id)
    if not old_employee:
        print("Employee not found")
    else:
        print(old_employee)
        if input('Are you sure to delete(y/n)?').upper() == 'Y':
                repo2.delete_employee(id)
                print(f'Employee deleted successfully')
  elif choice == 5:
    employees = repo2.read_all_employees()
    if len(employees) == 0:
      print('No employee exist.')
    else:
      print('List of Employees:')
      for employee in employees:
        print(employee)

  elif choice == 6:
     print("Exiting program")
     break
  else:
    print("Re-enter invalid choice")
