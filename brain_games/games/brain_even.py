"""Generation of questions and correct answers for brain-even game."""
from random import randint

from colorama import Fore as Color
from colorama import Style

from brain_games.games_logic import brain_games


def main(username):
    """
    Game data with question and correct answers.

    Parameters:
        username (str): user name
    """
    game_result = False
    while not game_result:
        conditions = ()
        while len(conditions) < 3:
            number = randint(1, 100)  # NOQA S311
            answer = 'yes' if number % 2 == 0 else 'no'
            conditions += ((number, answer),)
        game_result = brain_games(username, conditions)


GAME_RULES_TEXT = (
    'Answer {red}"yes"{reset} {bold}if{reset} number even otherwise answer ' +
    '{red}"no"{reset}{blue}.{reset}\n'
)
GAME_RULES = GAME_RULES_TEXT.format(
    red=Color.RED,
    blue=Color.BLUE,
    bold=Style.BRIGHT,
    reset=Style.RESET_ALL,
)
