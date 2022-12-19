import random


def get_random_num():
    '''Returns 2 values - a random number and whether it is even'''
    num = random.randint(1, 101)
    if num % 2 == 0:
        return num, 'yes'
    elif num % 2 != 0:
        return num, 'no'
