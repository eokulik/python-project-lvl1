"""Script that runs brain-calc game."""
from brain_games.games import brain_calc
from brain_games.scripts import brain_games


def main():
    """Step by step game run."""
    rules = brain_calc.GAME_RULES
    username = (brain_games.main(rules))
    brain_calc.main(username)
