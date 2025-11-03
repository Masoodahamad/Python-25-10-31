list = input("Enter number seperated by spaces")
list_num = list.split()
sum = 0
for num in list_num:
    sum += int(num)

avg = sum/len(list_num)

with open("qn2_data.txt", 'w') as output_file:
    output_file.write(f"list: {list}\n")
    output_file.write(f"sum: {sum}\n")
    output_file.write(f"Average: {avg}\n")

with open("qn2_data.txt", 'r') as input_file:
    list_str = input_file.readline()
    list_sum = input_file.readline()
    list_avg = input_file.readline()

print(list_str)
print(list_sum)
print(list_avg)