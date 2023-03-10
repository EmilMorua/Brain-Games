import random


MIN = 0
MAX = 101
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> str:
    """Accepts a number and returns whether it is a prime number"""

    if num < 3:
        return 'no'
    for divisor in range(2, num - 1):
        if num % divisor == 0:
            return 'no'
        return 'yes'


def game_launch() -> tuple:
    """Returns 2 values - a random number and whether it is a prime number"""

    num = random.randint(MIN, MAX)
    answer = is_prime(num)
    return num, answer
