#!/usr/bin/python3
def uniq_add(my_list = []):
    new_list = list()
    for i in range(len(my_list)):
        if not my_list[i] in new_list:
            new_list.append(my_list[i])
    return sum(new_list)
