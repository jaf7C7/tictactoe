from player import Player
from board import Board


class Tictactoe:

    def __init__(self):
        self.players = [Player(is_human=True), Player(is_human=False)]
        self.board = Board()
