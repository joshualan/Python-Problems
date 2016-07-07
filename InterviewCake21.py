"""This module contains solutions to the 21st problem of Interview Cake."""

import collections

def find_unique_delivery_id_n2(delivery_ids):
    """
    Finds the unique id in a list of ids with only one not having
    a duplicate

    This requires O(n) space
    This solution is a true O(n) since it doesn't use 'in', which is a O(n)
    so if you loop through the delivery_id's and then do an 'in' operator,
    that's O(n^2).
    """
    id_distribution = collections.defaultdict(int)

    for delivery_id in delivery_ids:
        id_distribution[delivery_id] += 1

    for delivery_id in delivery_ids:
        if id_distribution[delivery_id] == 1:
            return delivery_id

def find_unique_delivery_id_n(delivery_ids):
    """
    Finds the unique id in a list of ids with only one not having
    a duplicate

    So the smart thing to do here is to use XOR. Now, XOR is an
    operation that takes two bits and returns 1 if only 1 of these two bits
    is set to 1. The great thing about it is XOR'ing a number with the same
    number twice resets it back to the original number. So if we XOR
    this list by itself, the duplicates cancel each other out and leave us
    with the unique number!
    """
    unique_id = 0

    for delivery_id in delivery_ids:
        unique_id ^= delivery_id
