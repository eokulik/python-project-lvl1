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
        conditions += generate_conditions()
    brain_games(username, conditions)


def generate_conditions():
    """
    Generate game conditions.

    Returns:
         return (tuple): (question, correct_answer)
    """
    number = randint(1, 100)  # NOQA S311
    progression = randint(1, 10)  # NOQA S311
    hidden_position = randint(1, 10)  # NOQA S311
    return conditions_string(number, progression, hidden_position)


def conditions_string(number, progression, hidden_position):
    """
    Create tuple with question and answer.

    Parameters:
        number (int): number to start line
        progression (int): progression step
        hidden_position (int): position that will be hudden

    Returns:
        return (tuple): (question, correct_answer)
    """
    i = 1  # NOQA WPS111
    numbers_line = ''
    answer = ''
    while i <= 10:
        if i != 0:
            numbers_line += ' '  # NOQA WPS336
        if i == hidden_position:
            numbers_line += '..'  # NOQA WPS336
            answer = str(number)
        else:
            numbers_line += str(number)
        number += progression
        i += 1  # NOQA WPS111
    return ((numbers_line, answer),)
