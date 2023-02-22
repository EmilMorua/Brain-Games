import random


MIN = 0
MAX = 101


def is_prime(num):
    if num < 3:
        return 'no'
    for divisor in range(2, num - 1):
        if num % divisor == 0:
            return 'no'
        return 'yes'


def start_prime():
    '''Returns 2 values - a random number and whether it is prime'''

    num = random.randint(MIN, MAX)
    answer = is_prime(num)
    return num, answer
