from board import Board, make_ship_positions


def main():
    print 'EMPTY 5x5 BOARD'
    game_board = Board(size_x=5, size_y=5)
    print game_board
    raw_input()
    print 'HORIZONTAL SHIP'
    positions = make_ship_positions(start_x=1, start_y=1, is_horizontal=True, name='SHIP3')
    game_board.place_ship(positions)
    print game_board
    raw_input()
    print 'SUBMARINE'
    positions = make_ship_positions(start_x=4, start_y=1, is_horizontal=False, name='SUBMARINE')
    game_board.place_ship(positions)
    print game_board
    raw_input()
    print 'MISSED ATTACK'
    print game_board.attack(0, 0)  # MISS
    print game_board.attack(0, 0)  # ALREADY_TAKEN
    print game_board
    raw_input()
    print 'SUNK SHIP'
    print game_board.attack(1, 1)  # HIT
    print game_board.attack(2, 1)  # HIT
    print game_board.attack(3, 1)  # SUNK
    print game_board
    raw_input()
    print 'WIN GAME'
    print game_board.attack(4, 1)  # HIT
    print game_board.attack(4, 1)  # ALREADY_TAKEN
    print game_board.attack(4, 2)  # HIT
    print game_board.attack(4, 3)  # HIT
    print game_board.attack(4, 4)  # WIN
    print game_board

if __name__ == '__main__':
    main()
