import random

def get_divisor(num1, num2):
    for divisor in range(num2, 0, -1):
            if (num2 % divisor == 0) and (num1 % divisor == 0):
                return divisor


def get_nums_and_divisor(num1=random.randint(1, 101), num2=random.randint(1, 101)):
    '''Returns 2 numbers and their greatest common divisor'''
    divisor = get_divisor(num1, num2)
    return f'{num1} {num2}', divisor
