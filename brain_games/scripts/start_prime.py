from brain_games.games_script import start_game
from brain_games.games.brain_prime import start_prime
from brain_games.games.brain_prime import RULES


def main():
    start_game(start_prime, RULES)


if __name__ == '__main__':
    main()
