list_name = input("Enter names seperated by spaces : ").split()
list_name.sort()
names_tuple = tuple(list_name)

with open("names_data.txt", 'w') as output_file:
    output_file.write(f"List : {list_name}\n")
    output_file.write(f"Tuple : {names_tuple}")

with open("names_data.txt", 'r') as input_file:
    names_list = input_file.readline()
    name = input_file.readline()

print(names_list)
print(name)