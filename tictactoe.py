from player import Player
from board import Board


class Tictactoe:

    def __init__(self):
        self.player = Player(is_human=True)
        self.computer = Player(is_human=False)
        self.board = Board()

    def display(self, text):
        print(text)

    def play(self):
        while not self.game_over():
            self.play_round()

    def game_over(self):
        return self.board.winning_marker() is not None or self.board.is_full()
