# def dict_to_list(dict_to_convert):
#     list_for_convertion = []
#     for k, v in dict_to_convert.items():
#         if type(v) == int:
#             v *= 2
#         list_for_convertion.append((k, v))
#     return list_for_convertion


# print(dict_to_list({'a': 5, 'b': [], 'c': 100}))

#  ========================================================================================================================================================

def filter_list(list_to_filter, value_type):
    filtered_list = []
    for element in list_to_filter:
        if type(element) == value_type:
            filtered_list.append(element)

    return filtered_list

print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))
