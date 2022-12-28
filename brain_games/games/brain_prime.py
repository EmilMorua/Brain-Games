import random


def is_prime(num):
    if num < 3:
        return 'no'
    for divisor in range(2, num - 1):
        if num % divisor == 0:
            return 'no'
        return 'yes'


def get_num(num = random.randint(1, 101)):
    '''Returns 2 values - a random number and whether it is prime'''
    answer = is_prime(num)
    return num, answer
