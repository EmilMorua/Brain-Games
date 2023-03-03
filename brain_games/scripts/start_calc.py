from brain_games.games_script import start_game
from brain_games.games.brain_calc import start_calc
from brain_games.games.brain_calc import RULES


def main():
    start_game(start_calc, RULES)


if __name__ == '__main__':
    main()
