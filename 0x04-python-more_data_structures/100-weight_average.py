#!/usr/bin/python3
def weight_average(my_list = []):
    if not my_list:
        return 0
    average= 0.0
    init_list = list(t[0] * t[1] for t in my_list)
    weight_list = list(t[1] for t in my_list)
    average = sum(init_list) / sum(weight_list)
    return average
