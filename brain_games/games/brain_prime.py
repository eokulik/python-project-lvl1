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
        number = randint(1, 100)  # NOQA S311
        answer = 'yes' if is_prime(number) else 'no'
        conditions += ((number, answer),)
    brain_games(username, conditions)


def is_prime(number):
    """
    Count if number is prime.

    Parameters:
        number (int): number to analyze

    Returns:
        return (bool)
    """
    divider = number
    no_remainder_count = 0
    while divider > 0:
        if number % divider == 0:
            no_remainder_count += 1
        divider -= 1
    return no_remainder_count == 2


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'
