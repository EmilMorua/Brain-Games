import prompt
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../', '../'))


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    return name
