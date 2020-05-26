"""Script that runs brain-calc game."""
from brain_games import engine, games


def main():
    """Step by step game run."""
    engine.run(games.calc)
