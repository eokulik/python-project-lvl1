
"""Brain games application."""

from brain_games.cli import welcome_user


def main():
    """Call to necessary functions."""
    print('Welcome to the Brain Games!') # NOQA WPS421
    welcome_user()


if __name__ == '__main__':
    main()
