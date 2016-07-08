"""This module contains solutions to Problem 28 of Interview Cake."""

def paren_matcher(string, index):
    paren_count = 0
    for i in range(index+1, len(string)):
        if string[i] == ')': 
            if not paren_count:
                return i
            else:
                paren_count -= 1

        if string[i] == '(':
            paren_count += 1

s = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

assert paren_matcher(s, 10) == 79
