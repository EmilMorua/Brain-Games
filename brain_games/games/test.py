import prompt, random, sys


name = 'Emil'
def start_game(exercise: str, questions: list, answers: list) -> None:
    '''Accepts the conditions of the exercise, the list of questions and the list of answers. Plays the game and ends the game'''
    print(exercise)

    count_correct_answ = 0
    while (count_correct_answ < 3):
        print(f'Question: {questions[count_correct_answ]}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answers[count_correct_answ]):
            print('Correct!')
            count_correct_answ += 1
            continue
        sys.exit(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answers[count_correct_answ]}'.\nLet's try again, {name}!")

    print(f"Congratulations, {name}!")

def get_answer_prime(numbers: list) -> list:
    '''Accepts a list of numbers and returns a list with the answer to the question "Even prime?" for each number'''
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
print(questions)
answers = get_answer_prime(questions)
print(answers)

start_game(exercise, questions, answers)
