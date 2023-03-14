import random


MIN = 0
MAX = 101
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    """Accepts a number and returns whether it is a prime number"""

    if num < 4:
        return True
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


def game_launch() -> tuple:
    """Returns 2 values - a random number and whether it is a prime number"""

    num = random.randint(MIN, MAX)
    answer = is_prime(num)
    if answer:
        return num, 'yes'
    return num, 'no'
