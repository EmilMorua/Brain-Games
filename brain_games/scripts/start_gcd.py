from brain_games.games_script import start_game
from brain_games.games.brain_gcd import start_gcd
from brain_games.games.brain_gcd import RULES


def main():
    start_game(start_gcd, RULES)


if __name__ == '__main__':
    main()
