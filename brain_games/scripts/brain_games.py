"""Brain games application."""


from brain_games.cli import welcome_user


def main(game_rules=None):
    """
    Call to necessary functions.

    Parameters:
        game_rules (str): text that should be displayed as game rules

    Returns:
        return (str): username
    """
    print('Welcome to the Brain Games!')  # NOQA WPS421
    if game_rules:
        print(game_rules)  # NOQA WPS421
    return welcome_user()


if __name__ == '__main__':
    main()
