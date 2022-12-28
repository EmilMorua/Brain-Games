from brain_games.scripts.welcome_mass import main
from brain_games.scripts.games_script import start_game
from brain_games.games.brain_prime import get_num


if __name__ == '__main__':
    main()
    start_game(get_num)
