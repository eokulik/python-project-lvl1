"""Generation of questions and correct answers for brain-calc game."""

import operator
import random
from random import randint

RULES = 'What is the result of the expression?'
OPERATIONS = (
    (operator.add, '+'),
    (operator.sub, '-'),
    (operator.mul, '*'),
)


def generate_conditions():
    """
    Game data with question and correct answers.

    Returns:
        return (tuple): question, answer
    """
    number1, number2 = (randint(1, 100), randint(1, 100))
    operation_function, operation_sign = random.choice(OPERATIONS)
    question = '{0} {1} {2}'.format(
        number1,
        operation_sign,
        number2,
    )
    return question, operation_function(number1, number2)
