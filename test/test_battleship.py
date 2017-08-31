import outcomes
import battleship

def test_battleship():
    ship = battleship.Battleship(3)
    assert ship.hit_count == 0
    for i in range(2):
        assert ship.attack() == outcomes.HIT
        assert ship.hit_count == i + 1
    assert ship.attack() == outcomes.SUNK
    assert ship.hit_count == 3
