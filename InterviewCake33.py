"""This module contains solutions to Problem 33 of Interview Cake."""

def find_duplicate(list_of_nums):
    """
    In this word where there is a duplicate number, this function will stop
    at nothing to find it.
    """

    max_num = 0
    total = 0
    subtotal = 0

    for num in list_of_nums:
        max_num = max(max_num, num)
        total += num

    for num in range(max_num+1):
        subtotal += num

    return total - subtotal

num_list = [1, 2, 3, 4, 5, 2]
assert find_duplicate(num_list) == 2

num_list = [i for i in range(100000)]
num_list.insert(1234, 56755)
assert find_duplicate(num_list) == 56755
