from board import BoardTracker, Board, make_ship_positions
import outcomes
import cells
from nose.tools import assert_raises


def test_board_tracker():
    board_tracker = BoardTracker()
    assert board_tracker._battleships_not_sunk == 0
    for i in range(3):
        board_tracker.add_ship()
        assert board_tracker._battleships_not_sunk == i + 1
    for i in range(2):
        assert board_tracker.sink() == outcomes.SUNK
        assert board_tracker._battleships_not_sunk == 3 - i - 1
    assert board_tracker.sink() == outcomes.WIN
    assert board_tracker._battleships_not_sunk == 0


def test_board_empty():
    board = Board(3, 3)
    for x in range(3):
        for y in range(3):
            assert board.positions[y][x].state == cells.EMPTY
    assert board.board_tracker._battleships_not_sunk == 0


def test_board_place_ships():
    board = Board(3, 3)
    board.place_ship(iter([(0, 0), (0, 1)]))
    assert board.positions[0][0].state == cells.OCCUPIED
    assert board.positions[1][0].state == cells.OCCUPIED
    board.place_ship(iter([(1, 0), (2, 0)]))
    assert board.positions[0][1].state == cells.OCCUPIED
    assert board.positions[0][2].state == cells.OCCUPIED
    assert_raises(Exception, board.place_ship, iter([(2, 0), (2, 1)]))
    assert_raises(Exception, board.place_ship, iter([(2, 2), (2, 3)]))


def test_board_attack():
    board = Board(3, 3)
    board.place_ship(iter([(0, 0), (0, 1)]))
    board.place_ship(iter([(2, 2)]))
    assert board.attack(2, 2) == outcomes.SUNK
    assert board.attack(0, 0) == outcomes.HIT
    assert board.attack(1, 0) == outcomes.MISS
    assert board.attack(1, 0) == outcomes.ALREADY_TAKEN
    assert board.attack(0, 0) == outcomes.ALREADY_TAKEN
    assert board.attack(0, 1) == outcomes.WIN


def test_make_ship_positions():
    positions = list(make_ship_positions(0, 0, True, 'SHIP3'))
    assert positions == [(0, 0), (1, 0), (2, 0)]
    positions = list(make_ship_positions(0, 0, False, 'SHIP3'))
    assert positions == [(0, 0), (0, 1), (0, 2)]
    positions = list(make_ship_positions(0, 0, True, 'SUBMARINE'))
    assert positions == [(0, 0), (2, 0)]
    positions = list(make_ship_positions(0, 0, False, 'SUBMARINE'))
    assert positions == [(0, 0), (0, 2)]