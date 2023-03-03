import prompt
import brain_games.cli
import brain_games.scripts.welcome_mass


def start_game(game, RULES, max_point=3) -> None:
    '''Accepts a function from the selected game module.
    Plays the game and ends the game'''

    brain_games.scripts.welcome_mass.main()
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
                     f"Let's try again, {brain_games.cli.name}!")
            exit()

    print(f"Congratulations, {brain_games.cli.name}!")
    exit()
