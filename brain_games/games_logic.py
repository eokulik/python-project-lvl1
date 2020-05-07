"""Logic for the brain games."""

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
    elif name == 'brain-calc':
        return 'What is the result of the expression?\n'
    elif name == 'brain-gcd':
        return 'Find the greatest common divisor of given numbers.\n'
    elif name == 'brain-progression':
        text = 'What number is missing {bold}in{reset} the progression?\n'
        return text.format(bold=Style.BRIGHT, reset=Style.RESET_ALL)


def brain_games(username, conditions):
    """
    Logic of brain-even game.

    Parameters:
        username (str): username
        conditions (tuple): n pairs with (question, correct), n = game rounds

    Returns:
        return (bool): True if all answers were correct, False if
        user made error
    """
    for lap in conditions:
        question, correct = lap
        print("Question: {0}".format(question))  # NOQA WPS421
        answer = prompt.string('Your answer: {0}'.format(Color.BLUE))
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
            return False
    print('Congratulations, {}!'.format(username))  # NOQA WPS421
    return True
