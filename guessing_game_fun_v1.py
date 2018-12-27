"""guessing_game_fun_v1.py"""
"""Guessing Game with a function
In this project the guessing game is recast using a function
guessing_game_fun_v1 is version 1 of the Guessing Game"""

import random

computers_number = random.randint(1,100)
PROMPT = 'What is your guess? '

def do_guess_round():
    """Choose a random number, ask the user for a guess
    check whether the guess is true
    and reapeat until user is correct"""
    while True:
        players_guess = input(PROMPT)
        if computers_number == int(players_guess):
            print('Correct!')
            break
        elif computers_number > int(players_guess):
            print('Too low')
        else:
            print('Too high')
while True:
    do_guess_round()
