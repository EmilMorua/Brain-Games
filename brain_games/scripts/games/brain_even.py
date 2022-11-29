import prompt, random, sys
from brain_games.scripts.welcome_mass import main
from brain_games.scripts.games_script import start_game


main()
print('Answer "yes" if the number is even, otherwise answer "no".')

random_num = random.randint(1, 101)
condition1 = (random_num % 2 == 0)
question1 = random_num
answer1 = 'yes'
condition2 = (random_num % 2 != 0)
question2 = random_num
answer2 = 'no'

start_game(condition1, question1, answer1, condition2,
                question2, answer2)
