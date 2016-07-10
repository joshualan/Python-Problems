"""This module contains solutions to Problem 36 of Interview Cake."""

def find_if_deck_is_single_riffle(deck, half1, half2):
    index1 = 0 if half1 is not None else None
    index2 = 0 if half2 is not None else None

    if half1 is None and half2 is None and deck is not None:
        return False

    for card in deck:
        if index1 and card == half1[index1]:
            index1 += 1
        elif index2 and card == half2[index2]:
            index2 += 1
        else:
            return False

        if index1 >= len(half1):
            index1 = None

        if index2 >= len(half2):
            index2 = None

    return True
