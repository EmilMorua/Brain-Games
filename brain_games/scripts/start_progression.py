from brain_games.scripts.welcome_mass import main
from brain_games.scripts.games_script import start_game
from brain_games.games.brain_progression import get_progression



main()

start_game(get_progression)
