from player import Player
from board import Board


class Tictactoe:

    def __init__(self):
        self.players = [Player(is_human=True), Player(is_human=False)]
        self.board = Board()

    def play(self):
        self.display_message('Starting tictactoe...',)
        self.display_board()
        while True:
            for player in self.players:
                if player.is_human:
                    self.display_message('Enter your selection: ', end='')
                position = player.select_position()
                if position is None:
                    return
                if not player.is_human:
                    self.display_message(f"The computer selected `{position}'")
                try:
                    self.board.place_marker(player.marker, position)
                except Exception:
                    self.display_message(
                        'Invalid selection, not placing marker.'
                    )
                self.display_board()
                if self.board.winning_marker() is not None:
                    self.display_message('You win!')
                    return

    def display_message(self, message, **kwargs):
        print(message, **kwargs)

    def display_board(self):
        template = (
            ' {} | {} | {} \n'
            '---+---+---\n'
            ' {} | {} | {} \n'
            '---+---+---\n'
            ' {} | {} | {} '
        )
        self.display_message(template.format(*self.board.positions))
