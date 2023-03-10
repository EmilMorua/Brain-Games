import random


MIN = 0
MAX = 101
RULE = 'What is the result of the expression?'


def get_sums(num1: int, num2: int, operator: str) -> int:
    """Accepts 2 numbers, an operator to make a mathematical example,
    returns the answer to this expression"""

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def game_launch() -> tuple:
    """Returns 2 values - a random mathematical example and the answer to it"""

    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    answer = get_sums(num1, num2, random_operator)
    return f'{num1} {random_operator} {num2}', answer
