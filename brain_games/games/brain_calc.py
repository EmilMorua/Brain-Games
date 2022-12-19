import random


def get_sums():
    '''Returns 2 values - random math example and its answer'''
    num1 = random.randint(1, 101)
    num2 = random.randint(1, 101)
    random_operator = random.randint(1, 3)
    if random_operator == 1:
        return f'{num1} + {num2}', num1 + num2
    elif random_operator == 2:
        return f'{num1} - {num2}', num1 - num2
    elif random_operator == 3:
        return f'{num1} * {num2}', num1 * num2
