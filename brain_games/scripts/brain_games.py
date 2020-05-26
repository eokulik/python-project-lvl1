"""Brain games application."""


from brain_games.cli import welcome_user


def main():
    """
    Call to necessary functions.

    Returns:
        return (str): username
    """
    print('Welcome to the Brain Games!')
    return welcome_user()


if __name__ == '__main__':
    main()
