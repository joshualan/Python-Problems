"""This module contains solutions to Problem 40 of Interview Cake."""

def find_repeat(the_list):
    """Finds a repeat of a number in a list."""

    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:

        midpoint = (floor + ceiling) // 2

        lower_range_ceiling = midpoint
        upper_range_floor = midpoint + 1

        number_of_lower_range_nums = 0
        for num in the_list:
            if floor <= num <= lower_range_ceiling:
                number_of_lower_range_nums += 1

        # Now, if the total number of numbers is less than
        # the actual unique numbers in that range, that means
        # there's a duplicate. So iterate on that!
        if lower_range_ceiling - floor + 1 < number_of_lower_range_nums:
            ceiling = lower_range_ceiling
        else:
            floor = upper_range_floor

    return floor

print(find_repeat([1,4,4,3,2,5,6,7,8,9,10]))
