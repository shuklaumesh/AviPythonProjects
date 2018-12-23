"""We are going to make a guessing game in this file and in it's later vesions!"""


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
