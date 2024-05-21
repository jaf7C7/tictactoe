class Board:

    def __init__(self):
        self.positions = [
            None, None, None,
            None, None, None,
            None, None, None,
        ]

    def place_marker(self, marker, position):
        self.positions[position - 1] = marker
