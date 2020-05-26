"""Making package accessible as module."""
from brain_games.games import calc, even, gcd, prime, progression

__all__ = (  # NOQA WPS410
    'even',
    'calc',
    'gcd',
    'prime',
    'progression',
)
