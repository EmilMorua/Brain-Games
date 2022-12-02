import prompt
from brain_games.scripts.welcome_mass import main
import brain_games.cli


def start_game(exercise: str, questions: list, answers: list) -> None:
    '''Accepts the conditions of the exercise,
    the list of questions and the list of answers.
    Plays the game and ends the game'''
    main()
    print(exercise)

    count_correct_answ = 0
    while (count_correct_answ < 3):
        print(f'Question: {questions[count_correct_answ]}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answers[count_correct_answ]):
            print('Correct!')
            count_correct_answ += 1
            continue
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                     f"Correct answer was '{answers[count_correct_answ]}'.\n"
                     f"Let's try again, {brain_games.cli.name}!")
            exit()

    print(f"Congratulations, {brain_games.cli.name}!")
    exit()
