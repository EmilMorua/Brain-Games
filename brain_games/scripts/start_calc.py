from brain_games.scripts.welcome_mass import main
from brain_games.scripts.games_script import start_game
from brain_games.games.brain_calc import get_sums


if __name__ == '__main__':
    main()
    start_game(get_sums)
