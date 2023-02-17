import random


def is_even(num):
    if num % 2 == 0:
        return True
    return False


MIN = 0
MAX = 101


def start_even():
    '''Returns 2 values - a random number and whether it is even'''
    num = random.randint(MIN, MAX)
    if is_even(num) is True:
        return num, 'yes'
    return (num, 'no')
