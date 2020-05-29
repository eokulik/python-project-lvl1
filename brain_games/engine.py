"""Logic for the brain games."""

import prompt
from colorama import Fore as Color
from colorama import Style

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3
WRONG_ANSWER = (
                "{reset}{red}'{{answer}}'{reset} is wrong answer "
                + '{bold};({reset}{blue}.{reset} Correct answer was {red}'
                + "'{{correct}}'{reset}{blue}.{reset}"
                + "Let{red}'s try again, {{name}}!{reset}"
            ).format(
                red=Color.RED,
                blue=Color.BLUE,
                bold=Style.BRIGHT,
                reset=Style.RESET_ALL,
            )
CORRECT_ANSWER = 'Correct!'


def run(game):
    """
    Engine of brain games.

    Parameters:
        game (module): module of the game to run

    Returns:
        None if answer is incorrect

    """
    print('Welcome to the Brain Games!')
    print(game.RULES)
    print()
    username = welcome_user()
    for _ in range(ROUNDS_COUNT):  # NOQA WPS122
        question, correct = game.generate_conditions()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer != str(correct):
            text = WRONG_ANSWER.format(
                answer=answer,
                correct=correct,
                name=username,
            )
            print(text)
            return None
        print(CORRECT_ANSWER)
    print('Congratulations, {0}!'.format(username))
