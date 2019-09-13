#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    23 Mar 2019

    This is an ugly Python roulette board program. You start with 500 and can bet
    this amount against the Python random number generator.
    The program does input validation and prevents the user from entering
    strings and out of range numbers. Due to use of the modulo operator,
    you could choose to make the roulette board as large as you'd like, if
    you wanted to make gambling even less likely to have a favorable outcome.

    I could have used lists and tuples instead of the modulo operator,
    but I wasn't feeling very "Pythonic" today. Sorry Guido.
"""
import random
def int_input():
    good_input = False
    while good_input == False:
        good_value = input()
        try:
            val = int(good_value)
            good_input = True
        except ValueError:
            print("Please enter a number.")
    return good_value

def spin_wheel(pocket, wager):
    red = False
    black = False
    roll_red = False
    roll_black = False
    mod = pocket % 2
    win = -1
    color = ""
    if pocket >= 1 and pocket <= 10 or pocket >= 19 and pocket <= 28:
        if mod == 0:
            black = True
        else:
            red = True
    elif pocket != 0:
        if mod == 0:
            red = True
        else:
            black = True
    roll = random.randint(0, 36)
    roll_mod = roll % 2
    if roll >= 1 and roll <= 10 or roll >= 19 and roll <= 28:
        if roll_mod == 0:
            roll_black = True
            color = "black"
        else:
            roll_red = True
            color = "red"
    elif roll != 0:
        if roll_mod == 0:
            roll_red = True
            color = "red"
        else:
            roll_black = True
            color = "black"
    if pocket == 0 or roll == 0: # ugly override hack to prevent matching on 0
        red = False
        black = False
        roll_black = True
        roll_red = True
    if pocket == 0 and roll == pocket:
        win = 0 #green *10
        print("Green pocket! You win $"+(str(wager * 10)+"."))
    elif roll == pocket:
        win = 1 #pocket bet: *3
        print("Pocket "+str(pocket)+" match! Roll "+str(roll))
        print("You win $"+(str(wager * 3)+"."))
    elif red == roll_red or black == roll_black:
        print("Roulette board rolled "+str(roll)+", "+str(color)+" pocket.")
        print("Color match. You win $"+(str(wager * 2)+"."))
        win = 2 #match color: *2
    else:
        if roll == 0:
            print("Roulette board rolled "+str(roll)+", green pocket.")
        else:
            print("Roulette board rolled "+str(roll)+", "+str(color)+" pocket.")
        print("No color match. You lose $"+(str(wager)+"."))
        win = 3 #you lose
    return win

money = 500
pocket = -1
wager = -1
print("Welcome to Python Las Vegas. You are playing a simplified version of Roulette.")
print("You have $"+str(money)+" on hand.")
while money > 0:
    while pocket < 0 or pocket > 36:
        print("Please enter a pocket number, 0-36")
        pocket = int(int_input())
    while wager < 0:
        print("Please place your bet, $0 to $"+str(money)+".")
        wager = int(int_input())
    result = spin_wheel(pocket, wager)
    if result == 0:
        money = (wager * 10) + money
    elif result == 1:
        money = (wager * 3) + money
    elif result == 2:
        money = (wager * 2) + money
    else:
        money = money - wager
    pocket = -1
    wager = -1
print("You lose. The house always wins.")#the logical end result of gambling
