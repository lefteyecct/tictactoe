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

    while not letter == 'X' or not letter == 'O':
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

    while move not in [1,2,3,4,5,6,7,8,9] or not isEmpty(board, int(move)):

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