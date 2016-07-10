"""This module contains solutions to Problem 37 of Interview Cake."""

import random

def rand5():
    """This function generates a number between 1 to 5 using rand7()."""
    num = 6

    while num > 5:
        num = random.randint(1, 7)

    return num

assert rand5() < 6
