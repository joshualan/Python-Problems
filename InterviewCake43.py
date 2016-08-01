"""This module contains solutions to Problem 43 of Interview Cake."""

def merge_lists(list1, list2):
    """Merges two sorted lists."""

    index1 = index2 = 0
    sorted_list = []

    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] > list2[index2]:
            sorted_list.append(list2[index2])
            index2 += 1
        elif list1[index1] < list2[index2]:
            sorted_list.append(list1[index1])
            index1 += 1

    if index1 >= len(list1):
        sorted_list.extend(list2[index2:])
    else:
        sorted_list.extend(list1[index1:])

    return sorted_list

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

assert merge_lists(my_list, alices_list) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
