import random

board = [' ' for i in range(9)]

def print_board():
    print('-------------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
        print('-------------')

def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1 # adjust for 0-based indexing
            if move >= 0 and move < 9 and board[move] == ' ':
                board[move] = 'X'
                return
        except:
            pass
        print("Invalid move. Please try again.")

def computer_move():
    moves = [i for i in range(9) if board[i] == ' ']
    if len(moves) > 0:
        move = random.choice(moves)
        board[move] = 'O'

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def check_tie(board):
    for i in range(9):
        if board[i] == ' ':
            return False
    return True

print_board()
while True:
    player_move()
    print_board()
    if check_win(board, 'X'):
        print("You win!")
        break
    if check_tie(board):
        print("Tie game.")
        break
    computer_move()
    print_board()
    if check_win(board, 'O'):
        print("Computer wins.")
        break
    if check_tie(board):
        print("Tie game.")
        break