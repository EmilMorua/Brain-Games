import prompt, random, sys
from brain_games.cli import name


def start_game(condition1, question1, answer1, condition2,
                question2, answer2, condition3=0, question3=0, answer3=0):
    count_correct_answ = 0
    while (count_correct_answ < 3):
        if condition1:
            print(f'Question: {question1}')
            answer = prompt.string('Your answer: ')
            if answer == answer1:
                print('Correct!')
                count_correct_answ += 1
            sys.exit(f"'{answer}' is wrong answer ;(. Correct answer was '{answer1}'.\nLet's try again, {name}!")
        elif condition2:
            print(f'Question: {question2}')
            answer = prompt.string('Your answer: ')
            if answer == answer2:
                print('Correct!')
                count_correct_answ += 1
            sys.exit(f"'{answer}' is wrong answer ;(. Correct answer was '{answer2}'.\nLet's try again, {name}!")
        elif condition3:
            print(f'Question: {question3}')
            answer = prompt.string('Your answer: ')
            if answer == answer3:
                print('Correct!')
                count_correct_answ += 1
            sys.exit(f"'{answer}' is wrong answer ;(. Correct answer was '{answer3}'.\nLet's try again, {name}!")

    print(f"Congratulations, {name}!")
