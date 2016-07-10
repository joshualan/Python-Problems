"""This module contains solutions to Problem 32 of Interview Cake."""

def counting_sort(list_of_scores, highest_score):
    """Sorts a list of scores in log(n) time."""

    score_distribution = [0] * (highest_score+1)
    sorted_scores = []

    for score in list_of_scores:
        score_distribution[score] += 1

    for i in range(highest_score+1):
        sorted_scores.extend([i] * score_distribution[i])

    return sorted_scores
