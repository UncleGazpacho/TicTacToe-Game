from board import Board
from player import Player

if __name__ == '__main__':
    player_a = Player(1)
    player_b = Player(-1)
    board = Board()
    active_player = player_a

    while not board.is_full():
        board.print_board()
        try:
            cell = int(input('Where do you want to place your sign? [1-9]'))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 8:
            print('Please enter a number between 1 and 9!')
            continue
        if not board.make_turn(cell, active_player):
            print('Invalid move!')
            continue
        if board.check_win(active_player):
            board.print_board()
            print('You won!')
            break

        if active_player == player_a:
            active_player = player_b
        else:
            active_player = player_a