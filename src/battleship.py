import outcomes


class Battleship(object):
    """Class that represent a ship

    Attributes:
        length: integer for the length of the ship
        hit_count: number of hits
    """

    def __init__(self, length):

        self.length = length
        self.hit_count = 0

    def attack(self):
        """
        Handles an attack to the ship.

        If the ship is sunk in the attack pass control of the attack
        to the board_tracker.
        """
        self.hit_count += 1
        if self.hit_count == self.length:
            return outcomes.SUNK
        else:
            return outcomes.HIT

    def positions(self, *args, **kwargs):
        raise NotImplementedError(
            'cells method should be implemented in subclasses of Battleship')
