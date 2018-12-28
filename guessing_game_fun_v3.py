

import random

computers_number = random.randint(1.0,100.0)
PROMPT = 'What is your guess? '

def do_guess_round():
    """Choose a random number, ask the user for a guess
    check whether the guess is true
    and reapeat until user is correct"""
    computers_number = random.randint(1,1tyuiuytrtyu00)#Added
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
