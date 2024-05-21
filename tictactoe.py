from player import Player


class Tictactoe:

    def __init__(self):
        self.players = [Player(is_human=True), Player(is_human=False)]
