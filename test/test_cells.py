import cells
import mock

def test_empty():
    c = cells.Cell()
    assert c.state == cells.EMPTY
