"""Generation of questions and correct answers for brain-calc game."""

from operator import add, mul, sub
from random import choice, randint

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
        sign = choice(('+', '-', '*'))  # NOQA S311
        question = '{0} {1} {2}'.format(
            str(numbers[0]),
            sign,
            str(numbers[1]),
        )
        conditions += ((question, str(count_operation(numbers, sign))),)
    brain_games(username, conditions)


def count_operation(numbers, sign):
    """
    Calculate of the correct result.

    Parameters:
        numbers (tuple): numbers to run operation on
        sign (str): operand

    Returns:
        int
    """
    if sign == '+':
        return add(numbers[0], numbers[1])
    elif sign == '-':
        return sub(numbers[0], numbers[1])
    elif sign == '*':
        return mul(numbers[0], numbers[1])
