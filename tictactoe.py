from player import Player
from board import Board


class Tictactoe:

    def __init__(self, player_type=Player, board_type=Board):
        self.player_X = player_type(is_human=True, marker='X')
        self.player_O = player_type(is_human=False, marker='O')
        self.board = board_type()
        self.winner = None

    def display(self, text):
        print(text)

    def play(self):
        self.display(
            'Welcome to Tic-Tac-Toe!\n'
            '======================='
        )
        while not self.game_over():
            for player in self.player_X, self.player_O:
                self.display(self.board)
                if player.is_human:
                    self.display('Select an available position: ')
                position = player.select_position()
                if not player.is_human:
                    self.display(f'The computer selected position {position}')
                try:
                    self.board.place_marker(player.marker, position)
                except Exception:
                    self.display('Position not available, cannot place marker.')
        self.display(
            f'\n**** `{self.winner}` wins! ****\n'
            if self.winner
            else "\n**** It's a tie! ****\n"
        )

    def game_over(self):
        self.winner = self.board.winning_marker()
        return self.winner is not None or self.board.is_full()
