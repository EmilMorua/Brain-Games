import random


MIN = 0
MAX = 101


def is_even():
    num = random.randint(MIN, MAX)
    if num % 2 == 0:
        return (num, 'yes')
    return (num, 'no')


def start_even():
    '''Returns 2 values - a random number and whether it is even'''

    return is_even()
