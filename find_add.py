def find_sum_of_four(a, b, c, d, offset = 5, another_arg = 2):
    add_result = a + b + c + d + offset + another_arg
    mul_result = a * b * c * d * offset * another_arg
    return add_result, mul_result


print(find_sum_of_four(10, 20, 30, 40))
print(find_sum_of_four(c = 30, a = 10, d = 40, b = 20))
print(find_sum_of_four(10, 20, 30, 40, 6))
print(find_sum_of_four(10, 20, 30, 40, 6, 4))
print(find_sum_of_four(offset=3, c = 30, a = 10, d = 40, b = 20))
print(find_sum_of_four(offset=3, c = 30, a = 10, d = 40, b = 20, another_arg = 17))
print('End of program')

def find_sum(first, second, *others):
    '''
    find_sum takes arguments and returns sum of the two or many positiona arguments numbers
    '''
    add_result = first + second
    for num in others:
        add_result += num

    print(type(first), type(second), type(others), others)
    return add_result

print(find_sum(1, 2, 3, 4, 5))

def find_sum_ka(first, second, **others):
    '''
    find_sum takes arguments and returns sum of the two or many numbers in keywords args 
    '''
    add_result = first + second
    for keyword in others:
        add_result += others[keyword]

    print(type(first), type(second), type(others), others)
    return add_result

print(find_sum_ka(first=1, second=2, third=3, fourth=4, fifth=5))
