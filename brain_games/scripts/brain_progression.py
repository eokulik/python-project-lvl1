"""Script that runs brain-gcd game."""
from brain_games import games_logic
from brain_games.games import brain_progression
from brain_games.scripts import brain_games


def main():
    """Step by step game run."""
    rules = games_logic.game_rules('brain-progression')
    username = (brain_games.main(rules))
    brain_progression.main(username)
