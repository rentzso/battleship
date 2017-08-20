from mock import MagicMock

import outcomes
import battleship


def test_battleship():
    board_tracker = MagicMock()
    board_tracker.sink.return_value = outcomes.SUNK
    ship = battleship.Battleship(3, 0, 0, True, board_tracker)
    assert ship.hit_count == 0
    for i in range(2):
        assert ship.attack() == outcomes.HIT
        assert ship.hit_count == i + 1
    assert ship.attack() == outcomes.SUNK
    assert board_tracker.sink.called_once()
    assert ship.hit_count == 3
