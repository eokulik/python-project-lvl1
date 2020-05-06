"""Script that runs brain-even game."""
from brain_games import games_logic
from brain_games.scripts import brain_games


def main():
    """Step by step game run."""
    rules = games_logic.game_rules('brain-even')
    username = (brain_games.main(rules))
    games_logic.brain_even(username)
