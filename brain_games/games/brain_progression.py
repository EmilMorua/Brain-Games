import random
from brain_games.scripts.games_script import start_game


def get_progression() -> list:
    '''Returns a list
    whose first element is a sequence of 10 numbers with one gap,
    and whose second element is the missing number'''
    first_num = random.randint(1, 21)
    step = random.randint(1, 6)
    progression = [first_num]

    while (len(progression) < 10):
        progression.append(first_num + step)
        first_num += step

    missing_index = random.randint(0, 9)
    missing_number = progression.pop(missing_index)
    progression.insert(missing_index, '..')
    progression = ' '.join(str(v) for v in progression)
    return [progression, missing_number]


prog1 = get_progression()
prog2 = get_progression()
prog3 = get_progression()

exercise = 'What number is missing in the progression?'
questions = [prog1[0], prog2[0], prog3[0]]
answers = [prog1[1], prog2[1], prog3[1]]

start_game(exercise, questions, answers)
