from board import Board

def main():
    print 'EMPTY 5x5 BOARD'
    game_board = Board(size_x=5, size_y=5)
    print game_board
    raw_input()
    print 'HORIZONTAL SHIP'
    game_board.place_ship(length=3, start_x=1, start_y=1, is_horizontal=True)
    print game_board
    raw_input()
    print 'VERTICAL SHIP'
    game_board.place_ship(length=4, start_x=4, start_y=1, is_horizontal=False)
    print game_board
    raw_input()
    print 'MISSED ATTACK'
    print game_board.attack(0, 0) # MISS
    print game_board
    raw_input()
    print 'SUNK SHIP'
    print game_board.attack(1, 1) # HIT
    print game_board.attack(2, 1) # HIT
    print game_board.attack(3, 1) # SUNK
    print game_board

if __name__=='__main__':
    main()