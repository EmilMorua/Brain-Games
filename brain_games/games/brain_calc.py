import random


MIN = 0
MAX = 101


def get_sums(num1: int, num2: int, operator: str) -> int:
    """Accepts 2 numbers, an operator to make a mathematical example, returns the answer to this expression"""

    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    random_operator = random.randint(1, 3)
    if random_operator == '+':
        return num1 + num2
    elif random_operator == '-':
        return num1 - num2
    elif random_operator == '*':
        return num1 * num2


def start_calc() -> tuple:
    """Returns 2 values - a random mathematical example and the answer to it"""

    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    answer = get_sums(num1, num2, random_operator)
    return f'{num1} {random_operator} {num2}', answer
