from brain_games.games_script import start_game
from brain_games.games.brain_progression import start_progression
from brain_games.games.brain_progression import RULES



def main():
    start_game(start_progression, RULES)


if __name__ == '__main__':
    main()
