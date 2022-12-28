import prompt
from brain_games.scripts.welcome_mass import main
from brain_games.scripts.games_script import start_game
from brain_games.games.brain_even import get_random_num
from brain_games.games.brain_calc import get_sums
from brain_games.games.brain_gcd import get_nums_and_divisor
from brain_games.games.brain_prime import get_num
from brain_games.games.brain_progression import get_progression


def start():
    main()
    user_answer = prompt.string(
        '"Brain even", "Brain calc", "Brain gcd",\
        "Brain prime", "Brain progression"\n\
        Choose a game:  ')
    if user_answer == "Brain even":
        start_game(get_random_num)
    elif user_answer == "Brain calc":
        start_game(get_sums)
    elif user_answer == "Brain gcd":
        start_game(get_nums_and_divisor)
    elif user_answer == "Brain prime":
        start_game(get_num)
    elif user_answer == "Brain progression":
        start_game(get_progression)


if __name__ == '__main__':
    start()
