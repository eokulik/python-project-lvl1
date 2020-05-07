"""Script that runs brain-prime game."""
from brain_games.games import brain_prime
from brain_games.scripts import brain_games


def main():
    """Step by step game run."""
    rules = brain_prime.game_rules
    username = (brain_games.main(rules))
    brain_prime.main(username)
