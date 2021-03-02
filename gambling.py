##
# gambling.py
# Author: Matthew Kellett, Jacob Lum
# Created: 3/03/2021
# Version: 0.41
from random import *
choice = "y"
SUITS = ['♤', '♡', '♧', '♢']
history = ['♤', '♡', '♧', '♢']
bet = 0
BET_LIMITS = [0, 99999999]
REDBLACK_GUESS = ["black", "red"]
SUITS_GUESS = ["spades", "hearts", "clubs", "diamonds"]


# Bet function by Jacob
def money_input():
    bet = -1
    while bet <= BET_LIMITS[0] or bet >= BET_LIMITS[1]:
        while True:
            try:
                bet = float(input("How much would you like to bet?: "))
                break
            except:
                print("Please enter a number")
        if bet <= BET_LIMITS[0] or bet >= BET_LIMITS[1]:
            print("Please enter a reasonable bet")
    return bet

while choice != "n":

    # Error checking by Matthew
    while True:
        game = input("What game would you to play (redblack, suits): ")
        if game != "redblack" and game != "suits":
            print("ERROR: Please enter redblack or suits.")
        else:
            break

# Fancy box by Jacob
    print("History:")
    print("┏", "━"*len(history), "┓")
    print("┃", " ".join(history), "┃")
    print("┗", "━"*len(history), "┛")

    # Redblack by Matthew and Jacob
    if game == "redblack":
        if bet == 0:
            bet = money_input()
        else:
            print("Your bet is ${}".format(bet))
        # Redblack error checking by Jacob
        guess = "no"
        while guess not in REDBLACK_GUESS:
            guess = input("What do you guess? ").lower()
            if guess not in REDBLACK_GUESS:
                print("Please enter a valid guess")
        card = SUITS[randint(0, 3)]
        history.append(card)
        history.pop(0)

        # Redblack by Matthew
        print(card)
        if (SUITS.index(card) == 0 or SUITS.index(card) == 2 and
                guess == "black"):
            print("You won!")
            bet *= 2
        elif (SUITS.index(card) == 1 or SUITS.index(card) == 3 and
                guess == "red"):
            print("You won!")
            bet *= 2
        else:
            print("You lose!")
            bet = 0

    # Suits by Jacob and Matthew
    elif game == "suits":
        if bet == 0:
            bet = money_input()
        else:
            print("Your bet is ${}".format(bet))
        # Suits error checking by Matthew

        while True:
            guess = input("What do you guess? ")
            if guess not in SUITS_GUESS:
                print("ERROR: Please enter one of the suits\
 (diamonds, hearts, spades, clubs)")
            else:
                break
        card = SUITS[randint(0, 3)]
        history.append(card)
        history.pop(0)
        print(card)

        # Suits guess check by Jacob
        if SUITS.index(card) == SUITS_GUESS.index(guess):
                print("You Win")
                bet *= 4
        else:
            bet = 0
            print("You lose")

    # Check if user won or not
    if bet > 0:
        while True:
            choice = input("Your balance is {}. Would\
 you like to gamble? (y/n) ".format(bet))
            if choice == "n":
                print("You got ${}!".format(bet))
                break
            elif choice == "y":
                break
            else:
                print("ERROR: Please enter a proper answer (y/n)")
    else:
        print("GAME OVER")
        # Check if user wants to play again
        while True:
            choice = input("Do you want to play again? (y/n) ")
            if choice == "y":
                break
            elif choice == "n":
                print("Thanks for playing.")
                break
            else:
                print("ERROR: Please enter a proper answer (y/n) ")
