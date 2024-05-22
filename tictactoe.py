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
            ' {} | {} | {} \n'
            '---+---+---\n'
            ' {} | {} | {} \n'
            '---+---+---\n'
            ' {} | {} | {} \n'
        )
        print(template.format(*self.board.positions))
