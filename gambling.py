##
# gambling.py
# Author: Matthew Kellett, Jacob Lum
# Created: 3/03/2021
# Version: 0.2
choice = "y"
SUITS = ['♤', '♡', '♧', '♢']
history = ['♤', '♡', '♧', '♢']
bet = 0
from random import *
while choice != "n":
    game = input("What game would you to play (redblack, suits): ")

# Fancy box
    print("┏", "━"*len(history),"┓")
    print("┃"," ".join(history),"┃")
    print("┗", "━"*len(history),"┛")
    
    # Redblack
    if game == "redblack":
        if bet == 0:
            bet = float(input("How much do you want to bet? "))
        else:
            print("Your bet is ${}".format(bet))        
        guess = input("What do you guess? ")
        card = SUITS[randint(0,3)]
        history.append(card)
        history.pop(0)
        
        print(card)
        if card == "♡" or card == "♢":
            if guess == "red":
                print("You won!")
                bet *= 2
            else:
                print("You won!")
                bet *= 0
        elif card == "♤" or card == "♧":
            if guess == "black":
                print("You won!")
                bet *= 2
            else:
                print("You lost!")
                bet *= 0
        else:
            print("Something happened...")
            bet *= 0
    # Suits
    if game == "suits":
        if bet == 0:
            bet = float(input("How much do you want to bet? "))
        else:
            print("Your bet is ${}".format(bet))
        guess = input("What do you guess? ")
        card = SUITS[randint(0,3)]
        history.append(card)
        history.pop(0)
        print(card)
        if card == "♤" and guess == "spades":
            print("You won!")
            bet *= 4
        elif card == "♡" and guess == "hearts":
            print("You won!")
            bet *= 4
        elif card == "♧" and guess == "clubs":
            print("You won!")
            bet *= 4
        elif card == "♢" and guess == "diamonds":
            print("You won!")
            bet *= 4
        else:
            print("You lost!")
            bet *= 0

    if bet > 0:
        choice = input("Your balance is {}. Would you like to gamble? (y/n) ".format(bet))
        if choice == "n":
            print("You got ${}!".format(bet))
    else:
        print("GAME OVER")
        choice = "n"
            
            
        
