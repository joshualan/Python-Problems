"""This module contains solutions to Problem 30 of Interview Cake."""

import collections

def find_if_possible_palindome(string):
    word_distribution = collections.defaultdict(int)

    for ch in string:
        word_distribution[ch] += 1
        word_distribution[ch] %= 2

    num_single = 0

    for _, v in word_distribution.items():
        num_single += v

        if num_single > 1:
            return False

    return True

assert find_if_possible_palindome("a") is True
assert find_if_possible_palindome("civil") is False
assert find_if_possible_palindome("ivicc") is True
assert find_if_possible_palindome("rcarace") is True
