import outcomes

class Battleship(object):

    def __init__(self, length, start_x, start_y, is_horizontal, board_tracker):
        self.length = length
        self.start_x = start_x
        self.start_y = start_y
        self.is_horizontal = is_horizontal
        self.hit_count = 0
        self.board_tracker = board_tracker

    def attack(self):
        self.hit_count += 1
        if self.hit_count == self.length:
            return self.board_tracker.sink()
        else:
            return outcomes.HIT