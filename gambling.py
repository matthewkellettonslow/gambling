##
# gambling.py
# Author: Matthew Kellett, Jacob Lum
# Created: 2/03/2021
# Version: 0.1
choice = "y"
SUITS = ['♤', '♡', '♧', '♢']
history = ['♤', '♡', '♧', '♢']
bet = 0
from random import *
while choice != "n":
    game = input("""What game would you to play (redblack, suits): """)

# Fancy box
    print("┏", "━"*len(history),"┓")
    print("┃"," ".join(history),"┃")
    print("┗", "━"*len(history),"┛")
    
    # Redblack
    if game == "redblack":
        if bet == 0:
            bet = float(input("How much bet? "))
        else:
            print("Your bet is ${}".format(bet))        
        guess = input("What do you guess? ")
        card = SUITS[randint(0,3)]
        history.append(card)
        history.pop(0)
        
        print(card)
        if card == "♡" or card == "♢":
            if guess == "red":
                print("yes red")
                bet *= 2
            else:
                print("uh oh")
                bet *= 0
        elif card == "♤" or card == "♧":
            if guess == "black":
                print("yes black")
                bet *= 2
            else:
                print("uh oh")
                bet *= 0
        else:
            print("oh no")
            bet *= 0
    # Suits
    if game == "suits":
        if bet == 0:
            bet = float(input("How much bet? "))
        else:
            print("Your bet is ${}".format(bet))
        guess = input("What do you guess? ")
        card = SUITS[randint(0,3)]
        history.append(card)
        history.pop(0)
        print(card)
        if card == "♤" and guess == "spades":
            print("spades yes")
            bet *= 4
        elif card == "♡" and guess == "hearts":
            print("hearts yes")
            bet *= 4
        elif card == "♧" and guess == "clubs":
            print("clubs yes")
            bet *= 4
        elif card == "♢" and guess == "diamonds":
            print("diamonds yes")
            bet *= 4
        else:
            print("wrong")
            bet *= 0

    if bet > 0:
        choice = input("Your balance is {}. Would you like to gamble? (y/n) ".format(bet))
        if choice == "n":
            print("You got ${}!".format(bet))
    else:
        print("GAME OVER")
        choice = "n"
            
            
        
