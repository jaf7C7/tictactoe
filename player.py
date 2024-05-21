class Player:

    def __init__(self, is_human):
        self.is_human = is_human
        self.marker = 'X' if self.is_human else 'O'
