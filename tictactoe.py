import random

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerChoice():
    letter = ''

    while not (letter == 'X' or letter == 'O'):
        print('Please choose letter X or O?')
        letter = input().upper()

    # Set player’s letter and computer's letter.

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoFirst():
    
    # Randomly choose who goes first.

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    
    # yes returns Ture, otherwise False.

    print('Another round? (yes or no)')

    return input().lower().startswith('y')

def makeTheMove(board, letter, move):

    board[move] = letter

def winner(board, letter):
    
    # The function is to verify if the player wins, then returns True .

    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top

    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle

    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom

    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side

    (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle

    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side

    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal

    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def CopyBoard(board):
    
    # Copy the board list.

    dupeBoard = []

    for i in board:

        dupeBoard.append(i)

    return dupeBoard

def isEmpty(board, move):

    # Check if the board has empty space.

    return board[move] == ' '

def playersMove(board):

    # Get the play's input.

    move = ' '

    while move not in ['1','2','3','4','5','6','7','8','9'] or not isEmpty(board, int(move)):

        print('Pick a number for your next move? (1-9)')

        move = input()

    return int(move)

def pickMoveFromList(board, movesList):

    # Returns a valid move from the previous list and returns None if there is no valid move.

    possibleMoves = []

    for i in movesList:

        if isEmpty(board, i):

            possibleMoves.append(i)

    if len(possibleMoves) != 0:

        return random.choice(possibleMoves)
    else:
        return None

def computersMove(board, computerLetter):

    # Computer's next move in the board and return that value.

    if computerLetter == 'X':

        playerLetter = 'O'

    else:

        playerLetter = 'X'

# Algorithm for Tic Tac Toe AI:

    # Check if can win in the next move

    for i in range(1, 10):

        copy = CopyBoard(board)

        if isEmpty(copy, i):

            makeTheMove(copy, computerLetter, i)

            if winner(copy, computerLetter):

                return i

    # Check if the player could win then block the player.

    for i in range(1, 10):

        copy = CopyBoard(board)

        if isEmpty(copy, i):

            makeTheMove(copy, playerLetter, i)

            if winner(copy, playerLetter):

                return i

    # Take one of the corners if it's empty.

    move = pickMoveFromList(board, [1, 3, 7, 9])

    if move != None:

        return move

    # Take the center if it is empty.

    if isEmpty(board, 5):

        return 5

    # To one of the middle sides.

    return pickMoveFromList(board, [2, 4, 6, 8])

def isFull(board):

    # True if no more space. 

    for i in range(1, 10):

        if isEmpty(board, i):

            return False

    return True

print('Attendion! You are now starting Tic Tac Toe!')

while True:
    
    # Board reset 

    theBoard = [' '] * 10

    playerLetter, computerLetter = inputPlayerChoice()

    turn = whoFirst()

    print('The ' + turn + ' starts first.')

    gameIsOn = True

    while gameIsOn:

        if turn == 'player':

            # Player’s turn.

            drawBoard(theBoard)

            move = playersMove(theBoard)

            makeTheMove(theBoard, playerLetter, move)

            if winner(theBoard, playerLetter):

                drawBoard(theBoard)

                print('Congrats! Winner!')

                gameIsOn = False

            else:

                if isFull(theBoard):

                    drawBoard(theBoard)

                    print('You are not more clever than Algoritm!')

                    break

                else:

                    turn = 'computer'

        else:

            # Computer’s turn.

            move = computersMove(theBoard, computerLetter)

            makeTheMove(theBoard, computerLetter, move)

            if winner(theBoard, computerLetter):

                drawBoard(theBoard)

                print('Shame on you, looser!')

                gameIsOn = False

            else:

                if isFull(theBoard):

                    drawBoard(theBoard)

                    print('You are just as stupid as AI!')

                    break

                else:

                    turn = 'player'
    if not playAgain():

        break