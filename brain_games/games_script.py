import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello,', name)


def start_game(game, RULES, max_point=3) -> None:
    '''Accepts a function from the selected game module.
    Plays the game and ends the game'''

    welcome_user()
    print(RULES)
    count_correct_answer = 0
    while count_correct_answer < max_point:
        question, answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answer):
            print('Correct!')
            count_correct_answer += 1
            continue
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                     f"Correct answer was '{answer}'.\n"
                     f"Let's try again, {name}!")
            exit()

    print(f"Congratulations, {name}!")
    exit()
