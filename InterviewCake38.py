"""This module contains solutions to Problem 37 of Interview Cake."""

import random

def rand5():
    """Returns a random number from 1 to 5."""
    return random.randint(1, 5)

def rand7():
    """Uses rand5() to return a random number from 1 to 7."""
    counter = [0] * 6

    for idx in range(6):
        num = 3

        while num > 2:
            num = rand5()

        if num == 1:
            counter[idx] += num

    total = 0
    for count in counter:
        total += count

    return total + 1

for i in range(10000):
    assert 1 <= rand7() <= 7
