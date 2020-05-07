"""Generation of questions and correct answers for brain-gcd game."""
from random import randint

from brain_games.games_logic import brain_games


def main(username):
    """
    Game data with question and correct answers.

    Parameters:
         username (str): user name
    """
    conditions = ()
    while len(conditions) < 3:
        numbers = (randint(1, 100), randint(1, 100))  # NOQA S311
        question = '{0} {1}'.format(
            str(numbers[0]),
            str(numbers[1]),
        )
        conditions += ((question, str(calculate_answer(numbers))),)
    brain_games(username, conditions)


def calculate_answer(numbers):
    """
    Calculate correct answer.

    Parameters:
         numbers (tuple): numbers pair

    Returns:
        int
    """
    divider = min(numbers)
    while True:
        remainder = (numbers[0] % divider) + (numbers[1] % divider)
        if remainder == 0:
            break
        else:
            divider -= 1
    return divider


game_rules = 'Find the greatest common divisor of given numbers.\n'
