from player import Player
from board import Board


class Tictactoe:

    def __init__(self, player_type=Player, board_type=Board):
        self.player_X = player_type(is_human=True)
        self.player_O = player_type(is_human=False)
        self.board = board_type()

    def display(self, text):
        print(text)

    def play(self):
        while not self.game_over():
            self.play_round()

    def game_over(self):
        return self.board.winning_marker() is not None or self.board.is_full()
