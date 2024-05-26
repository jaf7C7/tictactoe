from unittest import TestCase
from unittest.mock import patch
from player import Player


class TestPlayer(TestCase):

    def test_is_human(self):
        human = Player(is_human=True)
        computer = Player(is_human=False)
        self.assertTrue(human.is_human and not computer.is_human)

    def test_markers(self):
        X = Player(marker='X')
        O = Player(marker='O')
        self.assertTrue(X.marker == 'X' and O.marker == 'O')

    @patch('player.input')
    def test_select_position_if_human(self, mock_input):
        human = Player(is_human=True)
        human.select_position()
        self.assertTrue(mock_input.called)

    def test_select_position_if_not_human(self):
        computer = Player(is_human=False)
        positions = []
        for i in range(10):
            positions.append(computer.select_position())
        self.assertTrue(all(1 <= p <= 9 for p in positions))
