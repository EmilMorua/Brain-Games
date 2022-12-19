import random


def get_nums_and_divisor():
    '''Returns 2 numbers and their greatest common divisor'''
    num1 = random.randint(1, 101)
    num2 = random.randint(1, 101)
    for divisor in range(num2, 0, -1):
        if (num2 % divisor == 0) and (num1 % divisor == 0):
            return f'{num1} {num2}', divisor
