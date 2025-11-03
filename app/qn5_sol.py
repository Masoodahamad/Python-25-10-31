num_list = input("Enter numbers : ").split()
nums = [int(num) for num in num_list]
max_num = max(nums)
min_num = min(nums)

with open("minmax_data.txt", 'w') as output_file:
    output_file.write(f"List : {nums}\n")
    output_file.write(f"Maximum: {max_num}\n")
    output_file.write(f"Minimum: {min_num}\n")
    
with open("minmax_data.txt", 'r') as input_file:
    list = input_file.readline()
    max = input_file.readline()
    min = input_file.readline()

print(list)
print(max)
print(min)
