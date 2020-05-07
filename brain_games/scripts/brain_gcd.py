"""Script that runs brain-gcd game."""
from brain_games.games import brain_gcd
from brain_games.scripts import brain_games


def main():
    """Step by step game run."""
    rules = brain_gcd.GAME_RULES
    username = (brain_games.main(rules))
    brain_gcd.main(username)
