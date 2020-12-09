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

