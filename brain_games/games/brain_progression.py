import random


def get_progression_with_a_pass(progression, missing_index = random.randint(0, 9)):
    missing_number = progression.pop(missing_index)
    progression.insert(missing_index, '..')
    progression = ' '.join(str(v) for v in progression)
    return progression, missing_number


def get_progression(first_num=random.randint(1, 21), step=random.randint(1, 6)) -> list:
    '''Returns 2 values - sequence of 10 numbers with one gap,
    and whose second element is the missing number'''
    progression = [first_num]

    while (len(progression) < 10):
        progression.append(first_num + step)
        first_num += step
    return get_progression_with_a_pass(progression)
