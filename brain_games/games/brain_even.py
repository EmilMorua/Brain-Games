import random
from brain_games.scripts.games_script import start_game


def check_even(numbers: list) -> list:
    '''Accepts a list of numbers and returns a list
    with the answer to the question "Even number?" for each number'''
    answers = []
    for num in numbers:
        if num % 2 == 0:
            answers.append('yes')
        elif num % 2 != 0:
            answers.append('no')
    return answers


num1 = random.randint(1, 101)
num2 = random.randint(1, 101)
num3 = random.randint(1, 101)

exercise = 'Answer "yes" if the number is even, otherwise answer "no".'
questions = [num1, num2, num3]
answers = check_even(questions)

start_game(exercise, questions, answers)
