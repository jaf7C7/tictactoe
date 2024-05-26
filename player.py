from random import randint


class Player:

    def __init__(self, is_human=None, marker=None):
        self.is_human = is_human
        self.marker = marker

    def select_position(self):
        return input() if self.is_human else randint(1, 9)
