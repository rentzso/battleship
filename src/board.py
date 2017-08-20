import cells
import outcomes
from battleship import Battleship


class Board(object):

    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.positions = []
        for y in range(size_y):
            row = []
            self.positions.append(row)
            for x in range(size_x):
                row.append(cells.Cell())
        self.board_tracker = BoardTracker()

    def place_ship(self, length, start_x, start_y, is_horizontal):
        i = 0
        ship_cells = []
        while (i < length):
            if is_horizontal:
                x = start_x + i
                y = start_y
            else:
                x = start_x
                y = start_y + i
            if not (self.size_x > x >= 0 and self.size_y > y >= 0):
                raise Exception('Cell is out of the board boundaries')
            elif self.positions[y][x].state == cells.EMPTY:
                ship_cells.append((x, y))
            else:
                raise Exception('Cell is not empty')
            i += 1
        battleship = Battleship(
            length, start_x, start_y,
            is_horizontal, self.board_tracker)
        self.board_tracker.add_ship()
        for x, y in ship_cells:
            self.positions[y][x].occupy(battleship)

    def attack(self, x, y):
        return self.positions[y][x].attack()

    def __str__(self):
        return '\n'.join([
            ' '.join([str(cell) for cell in row])
            for row in self.positions
        ])

class BoardTracker(object):

    def __init__(self):
        self._battleships_not_sunk = 0

    def add_ship(self):
        self._battleships_not_sunk += 1

    def sink(self):
        self._battleships_not_sunk -= 1
        if self._battleships_not_sunk == 0:
            return outcomes.WIN
        else:
            return outcomes.SUNK
