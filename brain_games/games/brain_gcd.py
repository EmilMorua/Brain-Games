import random


def get_divisor(num1, num2):
    for divisor in range(num2, 0, -1):
            if (num2 % divisor == 0) and (num1 % divisor == 0):
                return divisor


MIN = 0
MAX = 101

def start_gcd(num1, num2):
    '''Returns 2 numbers and their greatest common divisor'''

    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    divisor = get_divisor(num1, num2)
    return (f'{num1} {num2}', divisor)
