from random import randint


class Player:

    def __init__(self, is_human):
        self.is_human = is_human
        self.marker = 'X' if self.is_human else 'O'

    def select_position(self):
        if self.is_human:
            return input()
        else:
            return randint(1, 9)
