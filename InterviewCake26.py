"""This module contains solutions to Problem 26 of Interview Cake."""

def reverse_string(s):
    """Reverses a string in place."""
    lst = list(s)
    length = len(lst)
    for i in range(length):
        if i >= length - 1 - i:
            return ''.join(lst)

        tmp = lst[i]
        lst[i] = s[length-1-i]
        lst[length-1-i] = tmp

assert reverse_string("abcdefg") == "gfedcba"
assert reverse_string("abcdef") == "fedcba"
assert reverse_string("racecar") == "racecar"
