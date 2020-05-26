"""Generation of questions and correct answers for brain-gcd game."""
import math
from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_conditions():
    """
    Game data with question and correct answers.

    Returns:
        return (tuple): question, answer

    """
    number = randint(1, 100)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer


def is_prime(number):
    """
    Count if number is prime.

    Parameters:
        number (int): number to analyze

    Returns:
        return (bool)
    """
    for divider in range(2, int(math.sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True
