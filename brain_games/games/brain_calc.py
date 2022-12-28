import random


def sum(num1=random.randint(1, 101),
        num2=random.randint(1, 101),
        random_operator=random.randint(1, 3)):
    if random_operator == 1:
        return [1, num1, num2, num1 + num2]
    elif random_operator == 2:
        return [2, num1, num2, num1 - num2]
    elif random_operator == 3:
        return [3, num1, num2, num1 * num2]


def get_sums():
    '''Returns 2 values - random math example and its answer'''
    result = sum()
    if result[0] == 1:
        return f'{result[1]} + {result[2]}', result[3]
    elif result[0] == 2:
        return f'{result[1]} - {result[2]}', result[3]
    elif result[0] == 3:
        return f'{result[1]} * {result[2]}', result[3]
