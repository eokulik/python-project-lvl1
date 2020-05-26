"""Script that runs brain-prime game."""
from brain_games import engine, games


def main():
    """Step by step game run."""
    engine.run(games.prime)
