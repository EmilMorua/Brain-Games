import random
from brain_games.scripts.games_script import start_game


def get_random_sum() -> list:
    '''Returns a list from a random math example and its answer'''
    num1 = random.randint(1, 101)
    num2 = random.randint(1, 101)
    random_operator = random.randint(1, 3)
    if random_operator == 1:
        return [f'{num1} + {num2}', num1 + num2]
    elif random_operator == 2:
        return [f'{num1} - {num2}', num1 - num2]
    elif random_operator == 3:
        return [f'{num1} * {num2}', num1 * num2]


sums1 = get_random_sum()
sums2 = get_random_sum()
sums3 = get_random_sum()

exercise = 'What is the result of the expression?'
questions = [sums1[0], sums2[0], sums3[0]]
answers = [sums1[1], sums2[1], sums3[1]]

start_game(exercise, questions, answers)
