import random


def is_prime(num):
    if num < 3:
        return 'no'
    for divisor in range(2, num - 1):
        if num % divisor == 0:
            return 'no'
        return 'yes'


MIN = 0
MAX = 101

def start_prime(num):
    '''Returns 2 values - a random number and whether it is prime'''

    num = random.randint(MIN, MAX)
    answer = is_prime(num)
    return (num, answer)
