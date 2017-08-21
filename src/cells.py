import outcomes

# Possible values of the Cell state
EMPTY = 'EMPTY'
OCCUPIED = 'OCCUPIED'
MISS = 'MISS'
HIT = 'HIT'


class AttackStrategy(object):
    """Base class for all attack strategy of a cell"""

    @staticmethod
    def attack(cell):
        raise NotImplemented(
            'attack method should be implemented '
            'on subclasses of AttackStrategy'
        )


class AttackEmpty(AttackStrategy):
    """Strategy used when a cell is in state EMPTY"""

    @staticmethod
    def attack(cell):
        """Change the state to MISS and return the MISS outcome"""
        cell.state = MISS
        return outcomes.MISS

    def __str__(self):
        return 'E'


class AttackOccupied(AttackStrategy):
    """Strategy used when a cell is in state OCCUPIED"""

    @staticmethod
    def attack(cell):
        """Change the state to HIT and forward the attack to the cell ship"""
        cell.state = HIT
        return cell.battleship.attack()

    def __str__(self):
        return 'O'


class AttackMiss(AttackStrategy):
    """Strategy used when a cell is in state MISS"""

    @staticmethod
    def attack(cell):
        """Cell is already taken"""
        return outcomes.ALREADY_TAKEN

    def __str__(self):
        return 'M'


class AttackHit(AttackStrategy):
    """Strategy used when a cell is in state HIT"""

    @staticmethod
    def attack(cell):
        """Cell is already taken"""
        return outcomes.ALREADY_TAKEN

    def __str__(self):
        return 'X'


class Cell(object):
    """Class that represent a cell of the board game.

    Attributes:
        state: possible values are EMPTY, OCCUPIED, HIT and MISS
        battleship: battleship at the cell (set only if OCCUPIED or HIT)

    Class Attributes:
        strategy: dictionary that links states to attack strategies
    """
    strategy = {
        EMPTY: AttackEmpty(),
        OCCUPIED: AttackOccupied(),
        MISS: AttackMiss(),
        HIT: AttackHit()
    }

    def __init__(self):
        """Initialize as EMPTY"""
        self.state = EMPTY

    def occupy(self, battleship):
        """Place a battleship on the cell and set state to OCCUPIED"""
        self.battleship = battleship
        self.state = OCCUPIED

    def attack(self):
        """Run the attack using the strategy for the current state"""
        return self.strategy[self.state].attack(self)

    def __str__(self):
        return str(self.strategy[self.state])
