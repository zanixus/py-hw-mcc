#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    4 Mar 2019

    This is a quick rock-paper-scissors program. Lizard and Spock also make
    an appearance. Spock has improved his Vulcan conjecture since last time.
    Maybe he will beat Paper eventually, although I still don't
    know how he smashes scissors.

"""
import random
def tuple_input():
    print("Please enter 'Rock', 'Paper, 'Scissors', 'Lizard' or 'Spock'.")
    print("Any other input will default to 'Spock'.")
    user = input()
    user = user.lower().strip()
    if user == "rock":
        pick = 0
    elif user == "paper":
        pick = 1
    elif user == "scissors":
        pick = 2
    elif user == "lizard":
        pick = 3
    else:
        pick = 4
    return pick  
def win_test(player, cpu):
    print("You picked "+player.capitalize()+
          ", the computer picked "+cpu.capitalize()+".")
    if player == cpu:
        print("Same pick! Tie!")
    elif player == "rock":
        if cpu == "paper":
            print("You lose! Paper covers Rock!")
        elif cpu == "scissors":
            print("You win! Rock smashes Scissors!")
        elif cpu == "lizard":
            print("You win! Rock crushes Lizard!")
        elif cpu == "spock":
            print("You lose! Spock vaporizes Rock with his phaser!")
    elif player == "paper":
        if cpu == "rock":
            print("You win! Paper covers Rock!")
        elif cpu == "scissors":
            print("You lose! Scissors cut Paper!")
        elif cpu == "lizard":
            print("You lose! Lizard eats Paper!")
        elif cpu == "spock":
            print("You win! Paper disproves Spock's conjecture... for now.")
    elif player == "scissors":
        if cpu == "rock":
            print("You lose! Rock smashes Scissors!")
        elif cpu == "paper":
            print("You win! Scissors cut Paper!")
        elif cpu == "lizard":
            print("You win! Scissors decapitate Lizard!");
        elif cpu == "spock":
            print("You lose! Spock smashes Scissors!")
    elif player == "lizard":
        if cpu == "rock":
            print("You lose! Rock crushes Lizard!")
        elif cpu == "paper":
            print("You win! Lizard eats Paper!")
        elif cpu == "scissors":
            print("You lose! Scissors decapitate Lizard!")
        elif cpu == "spock":
            print("You win! Lizard poisons Spock!")
    else:
        if cpu == "rock":
            print("You win! Spock vaporizes Rock with his phaser!")
        elif cpu == "paper":
            print("You lose! Paper disproves Spock's conjecture... for now.")
        elif cpu == "scissors":
            print("You win! Spock smashes Scissors!");
        elif cpu == "lizard":
            print("You lose! Lizard poisons Spock!")
rps = ("rock", "paper", "scissors", "lizard", "spock")
win_test(rps[tuple_input()], rps[random.randrange(5)])
