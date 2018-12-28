"""guessing_game_fun_v3.py"""
"""Guessing Game with a function
In this project the guessing game is recast using a function
guessing_game_fun_v3 is version 3 of the Guessing Game"""
import random

PROMPT = 'What is your guess? '

def do_guess_round():
    """Choose a random number, ask the user for a guess
    check whether the guess is true
    and reapeat until user is correct"""
    computers_number = random.randint(1,100)
    number_of_guesses = 0#Added
    while True:
        players_guess = input(PROMPT)
        number_of_guesses = number_of_guesses+1#Added
        if computers_number == int(players_guess):
            print('Correct!')
            return number_of_guesses#Changed
        elif computers_number > int(players_guess):
            print('Too low')
        else:
            print('Too high')

total_rounds = 0#Added
total_guesses = 0#Added


while True:
    total_rounds = total_rounds+1#Added
    print("Round number: "+str(total_rounds))#Changed
    print("Let the guessing begin!!!")
    this_round = do_guess_round()#Changed
    total_guesses = total_guesses+this_round#Added
    print("You took "+str(this_round)+" guesses")#Added
    avg = str(total_guesses/float(total_rounds))#Added
    print("Your guessing average = "+avg)#Added
    print("")#blank line
