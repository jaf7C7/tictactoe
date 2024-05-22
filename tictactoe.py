from player import Player
from board import Board


class Tictactoe:

    def __init__(self):
        self.players = [Player(is_human=True), Player(is_human=False)]
        self.board = Board()

    def play(self):
        while True:
            if self.players[0].select_position() is None:
                break

    def display_message(self, message):
        print(message)

    def display_board(self):
        template = (
            'Board:\n'
            '\n'
            ' 1 | X | 3 \n'
            '---+---+---\n'
            ' O | 5 | 6 \n'
            '---+---+---\n'
            ' 7 | 8 | 9 \n'
        )
        print(template.format(self.board.positions))
