from employee import employees
import repo1 
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
    print("Enter Role")
    role = input()
    print("Enter Salary:")
    salary = input()
    repo1.add_employee({"id" : id, "name" : name, "role" : role, "salary" : salary})
  elif choice == 2:
    print("Enter id to search:")
    id = int(input())
    index = repo1.search_employee(id)
    if index != -1:
       print("Searched Employee: ", employees[index])
    else:
        print("Employee not found")
  elif choice == 3:
    print("Enter id to update")
    id = int(input())
    print("Enter salary to update")
    salary = int(input())
    repo1.update_employee(id, salary)
  elif choice == 4:
    print("Enter id to delete")
    id = int(input())
    index = repo1.search_employee(id)
    if index != -1:
        employees.pop(index)
        print("Employee deleted successfully")
    else:
        print("Employee not found")
  elif choice == 5:
    print(employees)
  elif choice == 6:
     print("Exiting program")
     break
  else:
    print("Re-enter invalid choice")
