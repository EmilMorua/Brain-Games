from brain_games.games_script import start_game
from brain_games.games.brain_even import start_even
from brain_games.games.brain_even import RULES


def main():
    start_game(start_even, RULES)


if __name__ == '__main__':
    main()
