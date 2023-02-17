import random


def get_progression_with_a_pass(progression, missing_index):
    missing_number = progression.pop(missing_index)
    progression.insert(missing_index, '..')
    progression = ' '.join(str(v) for v in progression)
    return (progression, missing_number)


FIRST_NUM_MIN = 1
FIRST_NUM_MAX = 21
STEP_MIN = 1
STEP_MAX = 6
MISSING_INDEX_MIN = 0
MISSING_INDEX_MAX = 9

def start_progression() -> list:
    '''Returns 2 values - sequence of 10 numbers with one gap,
    and whose second element is the missing number'''

    progression = [random.randint(FIRST_NUM_MIN, FIRST_NUM_MAX)]
    step = random.randint(STEP_MIN, STEP_MAX)
    missing_index = random.randint(MISSING_INDEX_MIN, MISSING_INDEX_MAX)

    while (len(progression) < 10):
        progression.append(first_num + step)
        first_num += step
    return get_progression_with_a_pass(progression, missing_index)
