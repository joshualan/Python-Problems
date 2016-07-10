"""This module contains solutions to Problem 35 of Interview Cake."""

import random

def shuffle_list(the_list):
    """Shuffles a list in place."""

    # So what we do here is pretty clever. To shuffle the list in place,
    # we treat i+1 to n as the unshuffled pool. To decide what we put in
    # i, we just select an item from the pool and then set the pool to be
    # i+1 to n.
    for idx in range(the_list):
        point_of_switch = random.randint(idx, len(the_list)-1)

        the_list[idx] = the_list[point_of_switch]
