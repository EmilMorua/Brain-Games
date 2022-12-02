import random
from brain_games.scripts.games_script import start_game


def get_answer_prime(numbers: list) -> list:
    '''Accepts a list of numbers and returns a list
     with the answer to the question "Even prime?" for each number'''
    answers = []
    for num in numbers:
        if num < 3:
            answers.append('no')
        for divisor in range(2, num - 1):
            if num % divisor == 0:
                answers.append('no')
                break
        else:
            answers.append('yes')
    return answers


num1 = random.randint(1, 101)
num2 = random.randint(1, 101)
num3 = random.randint(1, 101)

exercise = 'Answer "yes" if given number is prime. Otherwise answer "no".'
questions = [num1, num2, num3]
answers = get_answer_prime(questions)

start_game(exercise, questions, answers)
