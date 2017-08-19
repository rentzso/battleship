import outcomes

EMPTY = 'EMPTY'
OCCUPIED = 'OCCUPIED'
MISS = 'MISS'
HIT = 'HIT'

class AttackStrategy(object):

    @staticmethod
    def attack(cell):
        raise NotImplemented('attack method should be implemented on subclasses of AttackStrategy')


class AttackEmpty(AttackStrategy):

    @staticmethod
    def attack(cell):
        cell.state = MISS
        return outcomes.MISS

    def __str__(self):
        return 'E'


class AttackOccupied(AttackStrategy):

    @staticmethod
    def attack(cell):
        cell.state = OCCUPIED
        return cell.battleship.attack()

    def __str__(self):
        return 'O'


class AttackMiss(AttackStrategy):

    @staticmethod
    def attack(cell):
        return outcomes.ALREADY_TAKEN

    def __str__(self):
        return 'M'


class AttackHit(AttackStrategy):

    @staticmethod
    def attack(cell):
        return outcomes.ALREADY_TAKEN

    def __str__(self):
        return 'X'


strategy = {
    EMPTY: AttackEmpty(),
    OCCUPIED: AttackOccupied(),
    MISS: AttackMiss(),
    HIT: AttackHit()
}

class Cell(object):

    def __init__(self):
        self.state = EMPTY

    def occupy(self, battleship):
        self.battleship = battleship
        self.state = OCCUPIED

    def attack(self):
        strategy[self.state].attack(self)

    def __str__(self):
        return str(strategy[self.state])
