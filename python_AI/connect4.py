rows = 5
columns = 7

########################

def printBoard(board):
    for i in range(rows):
        for j in range(columns):
            print(board[i][j],end=" ")
        print() #New line

def playerInput():
    y = input("Enter your column : ")
    if not y.isdigit():
        print("You entered a wrong value!")
        return playerInput()
    elif not int(y)>0:
        print("You entered a wrong value!")
        return playerInput()
    else:
        y=int(y)-1
        return y


def changeBoardSlot(board,player):
    y = playerInput()
    for i in range(rows): #Check each row from the bottom
        if board[rows-1-i][y] == 0: #Change the case if it's empty
            board[rows-1-i][y] = player
            return
    #If the column is full
    print("This column is full! Choose another one")
    changeBoardSlot(player)

def checkVerticalLine(board,x,y):
    if board[x][y]==board[x+1][y]==board[x+2][y]==board[x+3][y] and board[x][y] != 0:
        return True
    else:
        return False

def checkHorizontalLine(board,x,y):
    if board[x][y]==board[x][y+1]==board[x][y+2]==board[x][y+3] and board[x][y] != 0:
        return True
    else:
        return False

def checkDiagonalLeftLine(board,x,y):
    if board[x][y]==board[x+1][y-1]==board[x+2][y-2]==board[x+3][y-3] and board[x][y] != 0:
        return True
    else:
        return False

def checkDiagonalRightLine(board,x,y):
    if board[x][y]==board[x+1][y+1]==board[x+2][y+2]==board[x+3][y+3] and board[x][y] != 0:
        return True
    else:
        return False
    

def checkBoard(board):
    for i in range(rows):
        for j in range(columns):
            #checkHorizontal max is j=3
            #checkVertical max is i=1
            #checkDiagonal left and right max are i=1 j=3
            if j<=3:
                if checkHorizontalLine(board,i,j):
                    return (i,j)
            if i<=1:
                if checkVerticalLine(board,i,j):
                    return (i,j)
            if j>3 and i<=1: 
                if checkDiagonalLeftLine(board,i,j):
                    return (i,j)
            if j<=3 and i<=1:
                if checkDiagonalRightLine(board,i,j):
                    return (i,j)
    return False

def cleanBoard():
    return [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
]

def play():
    
    board = cleanBoard()
    print("Here's the board !")
    printBoard(board)

    while True:

        if not checkBoard(board):
            #Player One input
            print("Player one: ")
            changeBoardSlot(board,1)
            printBoard(board)

        if not checkBoard(board):
            #Player Two input
            print("Player two: ")
            changeBoardSlot(board,2)
            printBoard(board)

        #Check if someone won
        else:
            if board[checkBoard(board)[0]][checkBoard(board)[1]] == 1:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            
            #Ask the player if he wants to play again
            replay = "0"
            while replay != "y" and replay != "n":
                replay = input("Wanna play again ? y/n : ")
                if replay != "y" and replay != "n":
                    print("Please enter either y or n")
            print(replay)

            if replay == "y":
                board = cleanBoard()
                play()
            elif replay == "n":
                print("See you soon !")
                exit()

play()