"""Generation of questions and correct answers for brain-even game."""
from random import randint

from colorama import Fore as Color
from colorama import Style

RULES = (
    'Answer {red}"yes"{reset} {bold}if{reset} number even otherwise answer '
    + '{red}"no"{reset}{blue}.{reset}'
).format(
    red=Color.RED,
    blue=Color.BLUE,
    bold=Style.BRIGHT,
    reset=Style.RESET_ALL,
)


def generate_conditions():
    """
    Game data with question and correct answer.

    Returns:
        return (tuple): question, answer

    """
    number = randint(1, 100)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer
