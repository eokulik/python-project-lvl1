"""Generation of questions and correct answers for brain-gcd game."""
from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def generate_conditions():
    """
    Game data with question and correct answers.

    Returns:
        return (tuple): question, answer

    """
    num1, num2 = randint(1, 100), randint(1, 100)
    question = '{0} {1}'.format(
        num1,
        num2,
    )
    while num2:
        num1, num2 = num2, num1 % num2
    return question, num1
