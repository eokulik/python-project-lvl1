"""Script that runs brain-even game."""
from brain_games.games import brain_even
from brain_games.scripts import brain_games


def main():
    """Step by step game run."""
    rules = brain_even.game_rules
    username = (brain_games.main(rules))
    brain_even.main(username)
