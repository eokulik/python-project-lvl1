"""Logic for the brain games."""

from random import randint

import prompt
from colorama import Fore as Color
from colorama import Style


def game_rules(name):
    """
    Return rules for the game.

    Parameters:
        name (str): the name of the game

    Returns:
        return (str): with game rules
    """
    if name == 'brain-even':
        text = (
            'Answer {red}"yes"{reset} {bold}if{reset} number even otherwise' +
            ' answer {red}"no"{reset}{blue}.{reset}\n'
        )
        return text.format(
            red=Color.RED,
            blue=Color.BLUE,
            bold=Style.BRIGHT,
            reset=Style.RESET_ALL,
        )


def brain_even(username):
    """
    Logic of brain-even game.

    Parameters:
        username (str): username
    """
    i = 1  # NOQA WPS111
    while i in range(1, 4):
        number = randint(1, 100)  # NOQA S311
        print("Question: {0}".format(number))  # NOQA WPS421
        answer = prompt.string('Your answer: {0}'.format(Color.BLUE))
        correct = 'yes' if number % 2 == 0 else 'no'
        if answer == correct:
            print('{0}Correct!'.format(Style.RESET_ALL))  # NOQA WPS421
        else:
            text = (
                "{reset}{red}'{answer}'{reset} is wrong answer {bold};(" +
                "{reset}{blue}.{reset} Correct answer was {red}'{correct}'" +
                "{reset}{blue}.{reset}\nLet{red}'s try again, {name}!{reset}"
            )
            text = (text.format(
                red=Color.RED,
                blue=Color.BLUE,
                bold=Style.BRIGHT,
                reset=Style.RESET_ALL,
                answer=answer,
                correct=correct,
                name=username,
            ))
            print(text)  # NOQA WPS421
            i = 1  # NOQA WPS111
            continue
        i += 1  # NOQA WPS111
    print('Congratulations, {}!'.format(username))  # NOQA WPS421
