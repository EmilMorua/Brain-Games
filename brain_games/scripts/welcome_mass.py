#!/Users/chibis/code/Projects/Project 1/python-project-49/.venv/bin python3

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../', '../'))
from brain_games.cli import welcome_user


def greet():
    print("Welcome to the Brain Games!")


def main():
    greet()
    welcome_user()


if __name__ == '__main__':
    greet()
