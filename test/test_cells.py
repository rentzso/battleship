import cells
from mock import MagicMock


def test_empty():
    c = cells.Cell()
    assert c.state == cells.EMPTY
    c.attack()
    assert c.state == cells.MISS
    c.attack()
    assert c.state == cells.MISS


def test_occupied():
    c = cells.Cell()
    battleship = MagicMock()
    c.occupy(battleship)
    assert c.state == cells.OCCUPIED
    c.attack()
    battleship.attack.assert_called_once()
    assert c.state == cells.HIT
    c.attack()
    battleship.attack.assert_called_once()
