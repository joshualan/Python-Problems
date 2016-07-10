"""This module contains solutions to Problem 31 of Interview Cake."""

def get_all_permutations_recursively(string):
    length = len(string)

    def rec_get_permutations(permutations, idx):
        if idx == length:
            return permutations

        new_permutations = set()

        for permutation in permutations:
            for i in range(len(permutation)+1):
                new_permutations.add(
                    permutation[:i]
                    + string[idx]
                    + permutation[i:])

        return rec_get_permutations(new_permutations, idx+1)

    return rec_get_permutations(set(string[0]), 1)

s = get_all_permutations_recursively("cat")
assert s == set(["cat", "cta", "act", "atc", "tac", "tca"]) 
