from player import Player
from board import Board


class Tictactoe:

    def __init__(self):
        self.player = Player(is_human=True)
        self.computer = Player(is_human=False)
        self.board = Board()
