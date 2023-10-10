# a = {7, 8, 9, 10}

# a.add(13)

# b = {7, 13, 14, 15, 16}

# c = (a | b) - (a & b)

# d = list(c)

# print(d)

#  ========================================================================================================================================================


set_one = {10, 5, 7, 15, 100}

set_one.add(200)

set_two = {20, 7, 300, 100, 200}

intersected_set = set_one.intersection(set_two)
print(intersected_set)

my_list = list(intersected_set)
print(my_list)

print(set_one)
print(set_two)
