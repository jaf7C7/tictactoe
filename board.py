class Board:

    def __init__(self):
        self.positions = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9,
        ]

    def place_marker(self, marker, position):
        self.positions[position - 1] = marker

    def winning_marker(self):
        marker = None
        for a, b, c in (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ):
            if (
                self.positions[a] in {'X', 'O'}
                and self.positions[a] == self.positions[b] == self.positions[c]
            ):
                marker = self.positions[a]
                break
        return marker

    def is_full(self):
        return all(p in {'X', 'O'} for p in self.positions)
