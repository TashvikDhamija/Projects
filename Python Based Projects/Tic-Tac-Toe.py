import numpy as np

# Max Number of moves possible
MAX_MOVES = 9

# Printing the XO Grid
def printBoard(arr):
    # Row 0
    print(arr[0][0],"|",arr[0][1],"|",arr[0][2],"|")
    # Row 1
    print(arr[1][0],"|",arr[1][1],"|",arr[1][2],"|")
    # Row 2
    print(arr[2][0],"|",arr[2][1],"|",arr[2][2],"|")

# Combination Check Function
def match(arr):
    # check row combinations
    for row in arr:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return True
    # check column combinations
    for i in range(3):
        a = arr[:,i]
        if a[0] == a[1] == a[2] and a[0] != '-':
            return True
    # check diagonal combinations
    if arr[0][0] == arr[1][1] == arr[2][2] and arr[0][0] != '-':
        return True
    if arr[0][2] == arr[1][1] == arr[2][0] and arr[0][2] != '-':
        return True
    return False

# Initial Introduction to the Game
print("Welcome to Tic-Tac-Toe Console Version 1.0")
print("Player 1: X")
print("Player 2: O")

# Main Game
while True:

    res = np.array(['-']*9).reshape((3,3))       # game array

    print("Grid: ")                              # initial grid
    printBoard(res)
    moves = 1
    while moves <= MAX_MOVES:
        # Player 1
        if moves % 2 != 0:
            p1_input = list(map(int,input("Enter Row and Column for X: ").split()))
            try:
                if res[p1_input[0]-1][p1_input[1]-1] == '-':
                    res[p1_input[0]-1][p1_input[1]-1] = 'X'
                    moves+=1
                else:
                    print("Invalid Input")
            except IndexError:
                print("Invalid Input")
        # Player 2
        else:
            p2_input = list(map(int,input("Enter Row and Column for O: ").split()))
            try:

                if res[p2_input[0]-1][p2_input[1]-1] == '-':
                    res[p2_input[0]-1][p2_input[1]-1] = 'O'
                    moves+=1
                else:
                    print("Invalid Input")
            except IndexError:
                print("Invalid Input")

        printBoard(res)                         # Board after playing this chance

        # Check if a combination is made
        if match(res):
            if moves % 2 == 0:
                print("X WON!!!")
                print("****************************************")
            else:
                print("O WON!!!")
                print("****************************************")
            break

    # Check if Match is draw
    if moves == 9 and match(res) != True:
        print("Draw Match!!! Try Again")
    print("****************************************")

    # New Game
    new_game = input("Enter Y/y to play again: ")
    if new_game == 'Y' or new_game == 'y':
        continue
    else:
        break
print("****************************************")
print("Thank You for playing Tic-Tac-Toe Console Version 1.0")
print("****************************************")
