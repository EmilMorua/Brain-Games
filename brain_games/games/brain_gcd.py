import random


MIN = 0
MAX = 101
RULE = 'Find the greatest common divisor of given numbers.'


def get_divisor(num1: int, num2: int) -> int:
    """Accepts 2 numbers and returns their greatest common divisor"""

    for divisor in range(num2, 0, -1):
        if (num2 % divisor == 0) and (num1 % divisor == 0):
            return divisor


def game_launch() -> tuple:
    """Returns 2 numbers and their greatest common divisor"""

    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    divisor = get_divisor(num1, num2)
    return f'{num1} {num2}', divisor
