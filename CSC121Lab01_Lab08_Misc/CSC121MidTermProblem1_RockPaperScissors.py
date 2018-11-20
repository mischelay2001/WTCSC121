__author__ = 'Michele Johnson'


# Program Requirements
# Rock–paper–scissors is a game played between two people, in which each player chooses rock, paper or scissors.
# The player who chooses rock will beat another player who has chosen scissors ("rock crushes scissors") but will lose
# to one who has chosen paper ("paper covers rock").  A play of paper will lose to a play of scissors
# ("scissors cut paper"). If both players make the same choice, the game is tied. Write a Python program for two
# players to play a rock-paper-scissors game.  The program first asks player 1  to enter 'r' for rock, 'p' for paper or
# 's' for scissors.  Use an input validation loop to check player 1's choice immediately.  If player 1 has entered an
# invalid choice (i.e., choice that is not 'r', 'p' nor 's'), ask player 1 to re-enter his choice repeatedly until the
# choice entered is valid.  Do the same for player 2.  Then compare the chices entered by the two players and display
# the result of the game ("Player 1 wins", "Player 2 wins" or "Tie").


def main():
    # Call Functions
    info_to_user()
    player1 = get_player1()
    player2 = get_player2()
    determine_winner(player1, player2)


def info_to_user():
    # Introduce program
    print('Welcome to ROCK PAPER SCISSORS Game!!!\n')
    print('This is a two player game.')
    print('Each player will select a weapon via a weapon code from the list below:\n')
    print('\t\tWeapons List\n')
    print('Weapon Code\t\t\tWeapon')
    print('R\t\t\t\t\tRock')
    print('P\t\t\t\t\tPaper')
    print('S\t\t\t\t\tScissors\n')
    print('The most powerful weapon WINS!!!\n')
    print("Rock CRUSHES Scissors")
    print("Paper COVERS Rock")
    print("Scissors CUT Paper")
    print("\n***If players choose the same weapon, the game will be tied.\n")


def get_player1():
    # Validate if user input is an R, P, or S
    a_player1 = ""
    boolean_valid_entry = False
    while boolean_valid_entry is False:
        # Initial user input and test
        try:
            a_player1 = input('Player 1, please enter your weapon of choice from the list above: ')
            a_player1 = a_player1.upper()
            if a_player1 == "R" or a_player1 == "P" or a_player1 == "S":
                boolean_valid_entry = True
        # Initial input not validgpa=input("Enter")
        # Error message
        except:
            print('\nThe player did not enter a valid weapon from the list above.')
    # Output the weapon chosen
    if a_player1 == "R":
        print("\nPlayer 1\'s weapon of choice is Rock.")
    if a_player1 == "P":
        print("\nPlayer 1\'s weapon of choice is Paper.")
    if a_player1 == "S":
        print("\nPlayer 1\'s weapon of choice is Scissors.")
    print()
    return a_player1


def get_player2():
    # Validate if user input is an R, P, or S
    a_player2 = ""
    boolean_valid_entry = False
    while boolean_valid_entry is False:
        # Initial user input and test
        try:
            a_player2 = input('Player 2, please enter your weapon of choice from the list above: ')
            a_player2 = a_player2.upper()
            if a_player2 == "R" or a_player2 == "P" or a_player2 == "S":
                boolean_valid_entry = True
        # Initial input not valid
        # Error message
        except:
            print('\nThe player did not enter a valid weapon from the list above.')
    # Output the weapon chosen
    if a_player2 == "R":
        print("\nPlayer 2\'s weapon of choice is Rock.")
    if a_player2 == "P":
        print("\nPlayer 2\'s weapon of choice is Paper.")
    if a_player2 == "S":
        print("\nPlayer 2\'s weapon of choice is Scissors.")
    print()
    return a_player2


def determine_winner(b_player1, b_player2):
    # Find out who wins the game
    if b_player1 == b_player2:
        print("It's a Tie!!!")
    elif b_player1 == "R" and b_player2 == "S":
        print("Rock beats Scissors.  Player 1 Wins!!!")
    elif b_player1 == "S" and b_player2 == "P":
        print("Scissors beat Paper.  Player 1 Wins!!!")
    elif b_player1 == "P" and b_player2 == "R":
        print("Paper beats Rocks.  Player 1 Wins!!!")
    elif b_player2 == "R" and b_player1 == "S":
        print("Rock beats Scissors.  The b_player2 Wins!!!")
    elif b_player2 == "S" and b_player1 == "P":
        print("Scissors beat Paper.  The b_player2 Wins!!!")
    else:
        print("Paper beats Rocks.  The b_player2 Wins!!!")


main()
