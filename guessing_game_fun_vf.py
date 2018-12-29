"""guessing_game_fun_vf.py"""
"""Guessing Game with a function
In this project the guessing game is recast using a function
guessing_game_fun_v3 is the final version of the Guessing Game"""
import random

PROMPT = 'What is your guess?

CONFIRM_QUIT_MESSAGE

def confirm_quit():
    """Ask your user to confirm that they want to quit
    default to yes
    Return True(yes, quit)or False(no, don't quit)"""
    spam = raw_input(CONFIRM_QUIT_MESSAGE)

def do_guess_round():
    """Choose a random number, ask the user for a guess
    check whether the guess is true
    and reapeat until user is correct"""
    computers_number = random.randint(1,100)
    number_of_guesses = 0
    while True:
        players_guess = input(PROMPT)
        number_of_guesses = number_of_guesses+1
        if computers_number == int(players_guess):
            print('Correct!')
            return number_of_guesses
        elif computers_number > int(players_guess):
            print('Too low')
        else:
            print('Too high')

total_rounds = 0
total_guesses = 0


while True:
    total_rounds = total_rounds+1
    print("Round number: "+str(total_rounds))
    print("Let the guessing begin!!!")
    this_round = do_guess_round()
    total_guesses = total_guesses+this_round
    print("You took "+str(this_round)+" guesses")
    avg = str(total_guesses/float(total_rounds))
    print("Your guessing average = "+avg)
    print("")
