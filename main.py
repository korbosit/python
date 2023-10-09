# my_list = ['abc', 5, 10.5, True, [1]]

# print(my_list)

# my_list.pop(2)

# print(len(my_list))
# print(my_list)

# my_list.reverse()
# print(my_list)

# other_list = [True, {'a': 10}]

# my_list.extend(other_list)

# print(my_list)
# print(other_list)

#  ========================================================================================================================================================


first_list = [10, True, 'abc']
second_list = [[1, 2], {'b': True}]

merged_list = first_list + second_list
print(merged_list)

other_merged_list = first_list.__add__(second_list)
print(other_merged_list)

print(first_list)
print(second_list)
