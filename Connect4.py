
import numpy as np

ROW_COUNT = 6
COLUMN = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] == piece

def is_valid_location(board, col):
    return board[5][col] == 0

def print_board(board):
    print(np.flip(board, 0))
def winning_move(board, piece):
    #Check horizontal locations for win
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

for c in range(COLUMN_COUNT-3):
    for r in range(ROW_COUNT):
        if biard[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece abd board[r][c+3]
        return True

    # Check vertical locations for win
    for 'c' in range(COLUMN_COUNT-3):
    for 'r' in range(ROW_COUNT):
        if board[r][c] == piece and board and board
def print_board(board):
    print(np.flip(board, 0))

board =
board = create_board()
game_over = False
turn = 0


while not game_over
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move)(board, 1)
:
                print("PLAYER 1 Wins! CONGRATS!!")

    # Ask Player 2 Input
    else:
        col = int(input("Player 2 Make your Selection (0-6) :"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    turn += 1
    turn = turn % 2