#!/usr/bin/bash
def max_integer(my_list=[]):
    """finds the biggest integer of a list"""
    if len(my_list) == 0:
        return None
    i = len(my_list) - 1
    while (i > 0):
        j = 0
        while (j < i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            j += 1
        i -= 1
    return (my_list[len(my_list) - 1])
