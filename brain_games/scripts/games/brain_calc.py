import prompt, random, sys
from brain_games.scripts.welcome_mass import main
from brain_games.scripts.games_script import start_game

main()
print('What is the result of the expression?')

random_num = random.randint(1, 101)
operator = random.randint(1, 4)
condition1 = (operator == 1)
question1 = random_num + random_num
answer1 = random_num + random_num
condition2 = (operator == 2)
question2 = random_num - random_num
answer2 = random_num - random_num
condition3 = (operator == 3)
question3 = random_num * random_num
answer3 = random_num * random_num

start_game(condition1, question1, answer1, condition2,
                question2, answer2, condition3, question3, answer3)
