import random

def printBoard(board):
    for row in range(len(board)):
        print(*board[row])


def askUser(board):
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))
    while(board[row][column] != '_'):
        print("Spot taken, try again: ")
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                            "[left column: enter 0, middle column: enter 1, right column enter 2]"))   
    spot = [row, column]
    return spot


def checkWin(board):
    count = 0
    # check every row for a straight X or straight O
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 'X'):
                count+=1
            elif (board[i][j] == 'O'):
                count-=1
            else:
                count = 0
                break
        if (count == 3 or count == -3):
            return count
    
    count = 0
    # check every column for a straight X or straight O
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[j][i] == 'X'):
                count+=1
            elif (board[j][i] == 'O'):
                count-=1
            else:
                count = 0
                break
        if (count == 3 or count == -3):
            return count

    count = 0
    # check the left diagonal for a straight X or straight O
    for i in range(len(board)):
        if (board[i][i] == 'X'):
            count+=1
        elif (board[i][i] == 'O'):
            count-=1
        else:
            count = 0
            break
    if (count == 3 or count == -3):
        return count
    
    count = 0
    # check the right diagonal for a straight X or straight O
    for i in range(len(board)):
        if (board[i][len(board) - 1 - i] == 'X'):
            count+=1
        elif (board[i][len(board) - 1 - i] == 'O'):
            count-=1
        else:
            count = 0
            break

    return count


board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

printBoard(board)

# loop through turns
for turn in range(9):
    # let the user choose a spot
    if (turn % 2 == 0):
        print("Turn: X")
        spot = askUser(board)
        board[spot[0]][spot[1]] = 'X'
    else:
        print("Turn: O")
        spot = askUser(board)
        board[spot[0]][spot[1]] = 'O'  

    # populate the board using askUser's return value
    printBoard(board)

    # determine the winner
    count = checkWin(board);
    if (count == 3):
        print("X wins")
        exit()
    elif (count == -3):
        print("O wins")
        exit();

print("It's a tie!")
