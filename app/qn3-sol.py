list = input("Enter a sentence : ").split()
t = tuple(word.upper() for word in list)
with open('sentence_data.txt', 'w') as output_file:
    output_file.write(f"List : {list}\n")
    output_file.write(f"Tuple : {t}\n")

with open('sentence_data.txt', 'r') as input_file:
    list_str = input_file.readline()
    tuple_str = input_file.readline()

print(list_str)
print(tuple_str)