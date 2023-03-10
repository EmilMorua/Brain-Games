import random


FIRST_NUM_MIN = 1
FIRST_NUM_MAX = 21
STEP_MIN = 1
STEP_MAX = 6
MISSING_INDEX_MIN = 0
MISSING_INDEX_MAX = 9
RULE = 'What number is missing in the progression?'


def get_progression_with_a_pass(progression: list, missing_index: int) -> tuple:
    """Accepts progression and index
    Returns 2 values
    the progression with the missing number from the passed index
    and the missing number itself"""

    missing_number = progression.pop(missing_index)
    progression.insert(missing_index, '..')
    progression = ' '.join(str(v) for v in progression)
    return progression, missing_number


def game_launch() -> tuple:
    """Returns 2 values
    a sequence of 10 numbers with a missing number and a missing number"""

    first_num = random.randint(FIRST_NUM_MIN, FIRST_NUM_MAX)
    progression = [first_num]
    step = random.randint(STEP_MIN, STEP_MAX)
    missing_index = random.randint(MISSING_INDEX_MIN, MISSING_INDEX_MAX)

    while len(progression) < 10:
        progression.append(first_num + step)
        first_num += step
    return get_progression_with_a_pass(progression, missing_index)
