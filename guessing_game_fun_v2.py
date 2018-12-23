"""We are going to make a guessing game in this file and in it's later vesions!"""
"""This is a modified version of the earlier versions called guessing_game_fun_v2.py!"""

import random

computers_number = random.randint(1,100)
PROMPT = 'What is your guess? '

def do_guess_round():
    """Choose a random number, ask the user for a guess
    check whether the guess is true
    and reapeat until user is correct"""
    computers_number = random.randint(1,100)#Added
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
    #Print statments added
    print("Starting a new round")
    print("The computer's number should be "+str(computers_number))
    print("Let the guessing begin!!!")
    do_guess_round()
    print("")#blank line
