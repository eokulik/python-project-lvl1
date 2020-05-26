"""Generation of questions and correct answers for brain-gcd game."""
from random import randint

from colorama import Style

RULES = (
    'What number is missing {bold}in{reset} the progression?'.
    format(bold=Style.BRIGHT, reset=Style.RESET_ALL)
)

QUESTION_LEN = 11


def generate_conditions():
    """
    Generate game conditions.

    Returns:
         return (tuple): (question, correct_answer)
    """
    number = randint(1, 100)
    progression_step = randint(1, 10)
    hidden_position = randint(1, 10)
    return generate_progression(number, progression_step, hidden_position)


def generate_progression(number, progression_step, hidden_position):
    """
    Create tuple with question and answer.

    Parameters:
        number (int): number to start line
        progression_step (int): progression step
        hidden_position (int): position that will be hidden

    Returns:
        return (tuple): (question, correct_answer)
    """
    numbers_line = ()
    answer = ''
    for count in range(QUESTION_LEN):
        if count == hidden_position:
            numbers_line += ('..',)
            answer = number
        else:
            numbers_line += (str(number),)
        number += progression_step
        count += 1
    numbers_line = ' '.join(numbers_line)
    return numbers_line, answer
