from termcolor import cprint
from sys import exit
import random
import time

def show(game_board):
    for m in range(3):
        for n in range(3):
            if game_board[m][n] == 'x':
                cprint('x', 'red', end='\t')
            elif game_board[m][n] == 'o':
                cprint('o', 'green', end='\t')
            else:
                cprint(game_board[m][n], end='\t')
        print()

def check(game_board, start_time):
    for m in range(3):
        if game_board[m][0] == 'x' and game_board[m][1] == 'x' and game_board[m][2] == 'x':
            elapsed_time = time.time() - start_time
            cprint('Player x won and elapsed time is {}'.format(elapsed_time), 'red')
            exit()
        if game_board[m][0] == 'o' and game_board[m][1] == 'o' and game_board[m][2] == 'o':
            elapsed_time = time.time() - start_time
            cprint('Player o won and elapsed time is {}'.format(elapsed_time), 'green')
            exit()
    for n in range(3):
        if game_board[0][n] == 'x' and game_board[1][n] == 'x' and game_board[2][n] == 'x':
            elapsed_time = time.time() - start_time
            cprint('Player x won and elapsed time is {}'.format(elapsed_time), 'red')
            exit()
        if game_board[0][n] == 'o' and game_board[1][n] == 'o' and game_board[2][n] == 'o':
            elapsed_time = time.time() - start_time
            cprint('Player o won and elapsed time is {}'.format(elapsed_time), 'green')
            exit()
    if game_board[0][0] == 'x' and game_board[1][1] == 'x' and game_board[2][2] == 'x':
        elapsed_time = time.time() - start_time
        cprint('Player x won and elapsed time is {}'.format(elapsed_time), 'red')
        exit()
    if game_board[0][0] == 'o' and game_board[1][1] == 'o' and game_board[2][2] == 'o':
        elapsed_time = time.time() - start_time
        cprint('Player o won and elapsed time is {}'.format(elapsed_time), 'green')
        exit()
    if game_board[0][2] == 'x' and game_board[1][1] == 'x' and game_board[2][0] == 'x':
        elapsed_time = time.time() - start_time
        cprint('Player x won and elapsed time is {}'.format(elapsed_time), 'red')
        exit()
    if game_board[0][2] == 'o' and game_board[1][1] == 'o' and game_board[2][0] == 'o':
        elapsed_time = time.time() - start_time
        cprint('Player o won and elapsed time is {}'.format(elapsed_time), 'green')
        exit()
    if game_board[0][0] != '-' and game_board[0][1] != '-' and game_board[0][2] != '-' and game_board[1][0] != '-' and game_board[1][1] != '-' and game_board[1][2] != '-' and game_board[2][0] != '-' and game_board[2][1] != '-' and game_board[2][2] != '-':
        print('Draw two players and elapsed time is {}'.format(elapsed_time))

def two_player(game_board):
    start_time = time.time()
    while True:
        # Player 1
        while True:
            row = int(input('Enter row: '))
            col = int(input('Enter colomn: '))
            if game_board[row][col] == '-':
                game_board[row][col] = 'x'
                break
            else:
                print('This cell has chosen')
        show(game_board)
        check(game_board, start_time)
        # Player 2
        while True:
            row = int(input('Enter row: '))
            col = int(input('Enter colomn: '))
            if game_board[row][col] == '-':
                game_board[row][col] = 'o'
                break
            else:
                print('This cell has chosen')
        show(game_board)
        check(game_board, start_time)
        if not '-' in game_board:
            print('Draw two players')

def one_player(game_board):
    start_time = time.time()
    while True:
        # Player 1
        while True:
            row = int(input('Enter row: '))
            col = int(input('Enter colomn: '))
            if game_board[row][col] == '-':
                game_board[row][col] = 'x'
                break
            else:
                print('This cell has chosen')
        show(game_board)
        check(game_board, start_time)
        # Player computer
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if game_board[row][col] == '-':
                game_board[row][col] = 'o'
                break
            else:
                print('This cell has chosen')
        show(game_board)
        check(game_board, start_time)


if __name__ == '__main__':
    game_board = [['-' for n in range(3)] for m in range(3)]
    show(game_board)
    number_players = int(input('Enter number of players: '))
    if number_players == 2:
        two_player(game_board)
    elif number_players == 1:
        one_player(game_board)
