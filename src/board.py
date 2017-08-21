import cells
import outcomes
from battleship import Battleship

names = {
    'SHIP3': 3,
    'SHIP4': 4
}

def make_ship_positions(start_x, start_y, is_horizontal, name):
    if name == 'SUBMARINE':
        yield (start_x, start_y)
        if is_horizontal:
            yield (start_x + 2, start_y)
        else:
            yield (start_x, start_y + 2)
    elif name == 'SHIP3':
        i = 0
        while (i < names[name]):
            if is_horizontal:
                x = start_x + i
                y = start_y
            else:
                x = start_x
                y = start_y + i
            yield (x, y)
            i += 1


class Board(object):
    """Class that represents the board of the game.

    Attributes:
        size_x: horizontal size of the board
        size_y: vertical size of the board
        positions: list of lists that store a cell for
                   each (x, y) position in the board
        board_tracker: keep the global state of the board
    """

    def __init__(self, size_x, size_y):
        """Initialize Board with empty cells for all positions"""
        self.size_x = size_x
        self.size_y = size_y
        self.positions = []
        for y in range(size_y):
            row = []
            self.positions.append(row)
            for x in range(size_x):
                row.append(cells.Cell())
        self.board_tracker = BoardTracker()

    def place_ship(self, positions):
        """Place a ship on the board

        Parameters:
            length: integer for the length of the ship
            start_x: x coordinate of the upper left corner of the ship
            start_y: y coordinate of the upper left corner of the ship
            is_horizontal: boolean indicating if the ship is horizontal
        """
        # i = 0
        # ship_cells = []
        # while (i < length):
        #     if is_horizontal:
        #         x = start_x + i
        #         y = start_y
        #     else:
        #         x = start_x
        #         y = start_y + i
        #     if not (self.size_x > x >= 0 and self.size_y > y >= 0):
        #         raise Exception('Cell is out of the board boundaries')
        #     elif self.positions[y][x].state == cells.EMPTY:
        #         ship_cells.append((x, y))
        #     else:
        #         raise Exception('Cell is not empty')
        #     i += 1
        # battleship = Battleship(length)
        ship_cells = []
        for x, y in positions:
            if not (self.size_x > x >= 0 and self.size_y > y >= 0):
                raise Exception('Cell is out of the board boundaries')
            elif self.positions[y][x].state == cells.EMPTY:
                ship_cells.append((x, y))
            else:
                raise Exception('Cell is not empty')
        battleship = Battleship(len(ship_cells))
        self.board_tracker.add_ship()
        for x, y in ship_cells:
            self.positions[y][x].occupy(battleship)

    def attack(self, x, y):
        """Forward the attack to the cell at position (x, y)"""
        result = self.positions[y][x].attack()
        if result == outcomes.SUNK:
            result = self.board_tracker.sink()
        return result

    def __str__(self):
        return '\n'.join([
            ' '.join([str(cell) for cell in row])
            for row in self.positions
        ])


class BoardTracker(object):
    """Class that keeps global state of a board

    Parameters:
        _battleships_not_sunk: number of battleship remaining on the board
    """

    def __init__(self):
        """The board starts with no battleships"""
        self._battleships_not_sunk = 0

    def add_ship(self):
        """Increment the battleship count by one"""
        self._battleships_not_sunk += 1

    def sink(self):
        """
        Increment the battleship count by one.
        If the count goes to 0, end the game
        """
        self._battleships_not_sunk -= 1
        if self._battleships_not_sunk == 0:
            return outcomes.WIN
        else:
            return outcomes.SUNK
