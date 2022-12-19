import random


def get_num():
    '''Returns 2 values - a random number and whether it is prime'''
    num = random.randint(1, 101)
    if num < 3:
        return num, 'no'
    for divisor in range(2, num - 1):
        if num % divisor == 0:
            return num, 'no'
        else:
            return num, 'yes'
