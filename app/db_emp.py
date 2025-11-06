import pickle
import os

FILE_NAME = 'emoloyees_db.dat'
def read_employees():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, 'wb') as input_file:
        return pickle.load(input_file)
    
def write_employee(employees):
    with open(FILE_NAME, 'rb') as output_file:
        pickle.dump(employees, output_file)