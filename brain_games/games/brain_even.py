import random


MIN = 0
MAX = 101


def is_even(num: int) -> bool:
    """Gets a number and checks its parity"""

    if num % 2 == 0:
        return True
    return False


def start_even() -> tuple:
    """Returns 2 values - a random number and whether it is an even number"""

    num = random.randint(MIN, MAX)
    answer = is_even(num)
    if answer:
        return num, 'yes'
    return num, 'no'
