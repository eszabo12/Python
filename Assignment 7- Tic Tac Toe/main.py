# Elle Szabo
# ITP 115, Spring 2019
# Assignment 7
# eszabo@usc.edu
import random
import TicTacToeHelper

# Checks if a move is okay to make and returns error message
def isValidMove(boardList, spot):
    if str(spot).isdigit():
        if int(spot) > 8 or int(spot) < 0:
            return False
    if boardList[spot] == "x" or boardList[spot] == "o":
        return False
    else:
        return True
# Places the player letter into the specified spot
def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter
# Prints the board out nicely
def printPrettyBoard(boardList):
    for i in range(len(boardList)):
        if i == 2 or i == 5:
            print(boardList[i] + "\n-------------")
        elif i == 8:
            print(boardList[i] + "\n")
        else:
            print(boardList[i], " | ", end=" ")
# Runs a full game
def playGame():
    # Lets a player make a move
    def playerMove(boardList):
        spot = int(input("Player %s, pick a spot: " % playerLetter))
        while not isValidMove(boardList, spot):
            print("Invalid move, please try again.")
            spot = int(input("Player %s, pick a spot: " % playerLetter))
        updateBoard(boardList, spot, playerLetter)
        printPrettyBoard(boardList)
    # Lets a computer make a move
    def computerMove(boardList):
        spot = int(computerChoice(boardList))
        updateBoard(boardList, spot, playerLetter)
        print("Computer chose", str(spot) + ".")
        printPrettyBoard(boardList)
    #Generates a random place on the board for the computer to choose
    def computerChoice(boardList):
        validList = []
        for i in boardList:
            # Checks if it's a valid place to make a move
            if str(i).isdigit():
                validList += (i)
        computerChoice = random.choice(validList)
        return computerChoice
    # Initializing variables
    move_counter = 0
    boardList = []
    # Creating boardList
    for i in range(9):
        boardList += str(i)
    #Gets input from users
    computerOrUser = int(input("Would you like to play the computer or another user? (1 for computer, 2 for user) "))
    while computerOrUser != 1 and computerOrUser != 2:
        print("Invalid option. Try again")
        computerOrUser = int(input("Would you like to play the computer or another user? (1 for computer, 2 for user) "))
    letterChoice = int(input("Would you like to play as x or o? (1 for x, 2 for o) "))
    while letterChoice != 1 and letterChoice != 2:
        print("Invalid option. Try again")
        letterChoice = int(input("Would you like to play as x or o? (1 for x, 2 for o) "))
    # Loops through while the game hasn't ended yet
    while TicTacToeHelper.checkForWinner(boardList, move_counter) == "n":
        # Creates the player letter based on how many moves have gone by
        if move_counter % 2 == 0:
            playerLetter = "x"
        else:
            playerLetter = "o"
        # Moves 1 and 2 if the first player is the computer:
        if computerOrUser == 1 and letterChoice == 2:
            if playerLetter == "x":
                computerMove(boardList)
                move_counter += 1
                if TicTacToeHelper.checkForWinner(boardList, move_counter) != "n":
                    break
            elif playerLetter == "o":
                playerMove(boardList)
                move_counter += 1
        # If the first user isn't a computer
        else:
            if playerLetter == "x":
                playerMove(boardList)
                move_counter += 1
                if TicTacToeHelper.checkForWinner(boardList, move_counter) != "n":
                    break
            # If the second player is the computer
            if computerOrUser == 1 and letterChoice == 1:
                if playerLetter == "o":
                    computerMove(boardList)
                    move_counter += 1
                    if TicTacToeHelper.checkForWinner(boardList, move_counter) != "n":
                        break
            # If neither player is a computer
            else:
                if playerLetter == "o":
                    playerMove(boardList)
                    move_counter += 1
    # After the while loop is exited, gets the result
    result = TicTacToeHelper.checkForWinner(boardList, move_counter)
    # Prints the result
    if result == "o":
        print("Game Over!")
        print("Player o is the winner!")
    elif result == "x":
        print("Game Over!")
        print("Player x is the winner!")
    else:
        print("Game Over!")
        print("Stalemate reached!")
# Asks the player if they want to play again
def main():
    playAgain = "y"
    while playAgain.lower() == "y":
        playGame()
        playAgain = input("Would you like to play again? (y/n): ")
        # Error checks for input on playAgain
        while playAgain.lower() != "y" and playAgain.lower() != "n":
            print("Invalid value.")
            playAgain = input("Would you like to play again? (y/n): ")
        if playAgain == "n":
            print("Goodbye!")
main()
