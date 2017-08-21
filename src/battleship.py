import outcomes


class Battleship(object):
    """Class that represent a ship

    Attributes:
        length: integer for the length of the ship
        start_x: x coordinate of the upper left corner of the ship
        start_y: y coordinate of the upper left corner of the ship
        is_horizontal: boolean indicating if the ship is horizontal
        hit_count: number of hits
        board_tracker: instance of BoardTracker keeping the global
                       state of the ship board
    """

    def __init__(self, length, start_x, start_y, is_horizontal, board_tracker):

        self.length = length
        self.start_x = start_x
        self.start_y = start_y
        self.is_horizontal = is_horizontal
        self.hit_count = 0
        self.board_tracker = board_tracker

    def attack(self):
        """
        Handles an attack to the ship.

        If the ship is sunk in the attack pass control of the attack
        to the board_tracker.
        """
        self.hit_count += 1
        if self.hit_count == self.length:
            return self.board_tracker.sink()
        else:
            return outcomes.HIT
