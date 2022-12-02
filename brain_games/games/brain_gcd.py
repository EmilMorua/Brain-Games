import random
from brain_games.scripts.games_script import start_game


def get_largest_divisor(num1: int, num2: int) -> int:
    '''Takes 2 numbers and returns their greatest common divisor'''
    for divisor in range(num2, 0, -1):
        if (num2 % divisor == 0) and (num1 % divisor == 0):
            return divisor


num1 = random.randint(1, 101)
num2 = random.randint(1, 101)
num3 = random.randint(1, 101)
num4 = random.randint(1, 101)
num5 = random.randint(1, 101)
num6 = random.randint(1, 101)

exercise = 'Find the greatest common divisor of given numbers.'
questions = [f'{num1} {num2}', f'{num3} {num4}', f'{num5} {num6}']
answers = [
    get_largest_divisor(num1, num2),
    get_largest_divisor(num3, num4),
    get_largest_divisor(num5, num6)
]

start_game(exercise, questions, answers)
