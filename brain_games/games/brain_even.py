import random


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def get_random_num(num = random.randint(1, 101)):
    '''Returns 2 values - a random number and whether it is even'''
    if is_even(num) is True:
        return num, 'yes'
    return num, 'no'
