"""
Name: Aidan Stout
lab9.py
Problem: create a program to play tic-tac-toe
I certify that this lab is entirely my work
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(board[position - 1]).isnumeric():
        return True
    return False


def fill_spot(board, position, shape):
    shape = shape.strip()
    shape = shape.lower()
    board[position - 1] = shape


def game_is_won(board):
    for i in range(0, len(board), 3):  # rows
        if board[i] == board[i + 1] == board[i + 2]:
            return True

    for i in range(0, (len(board) - 6)):  # columns
        if board[i] == board[i + 3] == board[i + 6]:
            return True

    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    return False


def game_over(board):
    if game_is_won(board):
        return True
    for i in range(len(board)):
        if is_legal(board, i):
            return False
    return True


def get_winner(board):
    if not game_over(board):
        return None
    x_count = 0
    o_count = 0
    for i in range(len(board)):
        if i == 'x':
            x_count = x_count + 1
        if i == 'o':
            o_count = o_count + 1
    if x_count > o_count:
        return 'x'
    else:
        return 'o'


def play(board):
    print("Instructions: Players will take turns placing their shape (x or o) "
          "on a square by entering the number where they want to play.")
    play_again = 'y'
    while play_again.startswith('y'):
        while not game_over(board):
            position_x = eval(input("x's turn:"))
            if is_legal(board, position_x) is True:
                fill_spot(board, position_x, 'x')
            else:
                print("That spot is already taken. Pick again:")
            position_o = eval(input("o's turn:"))
            if is_legal(board, position_o) is True:
                fill_spot(board, position_o, 'o')
            else:
                print("That spot is already taken. Pick again:")
        if get_winner(board) == 'x':
            print("x's win!")
        if get_winner(board) == 'o':
            print("o's win!")
        if get_winner(board) is None:
            print("it's a tie!")
        play_again = input("do you want to play again?")


def main():
    play(build_board())


if __name__ == '__main__':
    main()
