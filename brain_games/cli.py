
"""CLI app."""

import prompt


def welcome_user():
    """
    Prompts user name and greets.

    Returns:
        return (str): username
    """
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name)) # NOQA WPS421
    return name
