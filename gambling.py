##
# gambling2.py
# Author: Matthew Kellett
# Created: 17/03/2021
# Version: 2.0
import random
history = ['♤', '♡', '♧', '♢']


# Game input function
def game_input():
    """
    Gets game choice from user
    """
    game = None
    GAME_CHOICES = ["colours", "suits"]
    # Gets game from user
    while game not in GAME_CHOICES:
        game = input("What game would you like to play? " +
                     "(suits, colours): ").lower()
        if game not in GAME_CHOICES:
            print("ERROR: Please enter one of the listed games")
    return game


# Bet input function
def bet_input():
    """
    Takes bet from user
    """
    BET_LIMITS = [0, 99999999]
    repeat = True
    # Takes bet from user
    while repeat == True:
        try:
            bet = float(input("How much would you like to bet?: "))
            if bet > BET_LIMITS[0] and bet < BET_LIMITS[1]:
                break
            else:
                raise ValueError
        except:
            print("Please enter a number above 0 and below 99,999,999.")
    return bet


# History function
def draw_history():
    """
    Prints out history of up to 4 from list
    """
    # add 4 rand values to history if empty
    if len(history) == 0:
        for i in range(0, 3):
            history.append(random.choice(SUITS))
    # print history
    print("History:")
    print("┏", "━"* 4, "┓")
    print("┃", " ".join(history), "┃")
    print("┗", "━"* 4, "┛")


def draw_card(SUITS):
    """
    Draws a card for gambling
    """
    # draw card
    card = random.choice(SUITS)
    return card

# Colours game guess
def colours_guess():
    """
    Gets a guess as an input from user
    for colours game
    """
    COLOURS_GUESSES = ["black", "red"]
    # Takes guess from user and checks for error
    guess = None
    while guess not in COLOURS_GUESSES:
        guess = input("What is your guess? (black, red): ").lower()
        if guess not in COLOURS_GUESSES:
            print("ERROR: Please enter a valid guess.")
        else:
            return guess


# Colours game win/lose
def colours_check(card, bet, guess, SUITS):
    """
    Checks if card drawn matches guess
    then returns bet for colours game
    """
    # Print "card" drawn from deck
    print("Card drawn: {}".format(card))
    SUITS.index(card) % 2
    # Check if guess is correct and output result
    if guess == "black" and SUITS.index(card) % 2 == 0:
        print("You won!")
        return bet * 2
    elif guess == "red" and SUITS.index(card) % 2 == 1:
        print("You won!")
        return bet * 2
    else:
        print("You lose...")
        return 0


# Suits game guess
def suits_guess(SUITS_GUESSES):
    """
    Gets a guess as an input from user
    for suits game
    """
    # Takes guess from user and checks for error
    guess = None
    while guess not in SUITS_GUESSES:
        guess = input("What is your guess? " +
                      "(spades, hearts, clubs, diamonds): ").lower()
        if guess not in SUITS_GUESSES:
            print("ERROR: Please enter a valid guess.")
        else:
            return guess


# Suits game win/lose
def suits_check(card, bet, guess, SUITS, SUITS_GUESSES):
    """
    Checks if card drawn matches guess
    then returns bet for suits game
    """
    # Print card drawn
    print("Card drawn: {}".format(card))
    # Check if guess is correct and output result
    if SUITS.index(card) == SUITS_GUESSES.index(guess):
        print("You win!")
        return bet * 4
    else:
        print("You lose...")
        return 0


# Checks if user wants to gamble/play again
def user_won(bet):
    """
    Checks if user wants to play again
    """
    gamble_choice = None
    repeat_choice = None

    if bet != 0:
        # Check if user wants to gamble
        while gamble_choice != "y" and gamble_choice != "n":
            gamble_choice = input("Your balance is ${}. Would ".format(bet) +
                           "you like to gamble? (y/n): ").lower()
            if gamble_choice == "y":
                return gamble_choice
            elif gamble_choice == "n":
                print("You got ${}!".format(bet))
                break
            else:
                print("ERROR: Please enter a proper answer")

    # Check if user wants to play again
    while repeat_choice != "y" and repeat_choice != "n":
        repeat_choice = input("Do you want to play again? (y/n): ").lower()
        if repeat_choice == "y" or repeat_choice == "n":
            print("Thanks for playing!")
            return repeat_choice
        else:
            print("ERROR: Please enter a proper answer")


# Gamble menu function
def gamble_menu():
    SUITS = ['♤', '♡', '♧', '♢']
    history = []
    SUITS_GUESSES = ["spades", "hearts", "clubs", "diamonds"]
    repeat_choice = None
    bet = 0

    # Get game, bet from user and print history
    while repeat_choice != "n":
        game = game_input()
        draw_history()
        card = draw_card(SUITS)
        if bet == 0:
            bet = bet_input()
        # If game is colours, play colours
        if game == "colours":
            guess = colours_guess()
            bet = colours_check(card, bet, guess, SUITS)
        # If game is suits, play suits.
        elif game == "suits":
            guess = suits_guess(SUITS_GUESSES)
            bet = suits_check(card, bet, guess, SUITS, SUITS_GUESSES)
        # Check if user won and ask if they want to play again
        repeat_choice = user_won(bet)

if __name__ == "__main__":
    gamble_menu()


