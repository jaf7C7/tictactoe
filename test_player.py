from unittest import TestCase
from unittest.mock import patch
from player import Player


class TestPlayer(TestCase):

    def test_is_human(self):
        human = Player(is_human=True)
        computer = Player(is_human=False)
        self.assertTrue(human.is_human)
        self.assertFalse(computer.is_human)

    def test_markers(self):
        human = Player(is_human=True)
        computer = Player(is_human=False)
        self.assertEqual('X', human.marker)
        self.assertEqual('O', computer.marker)

    @patch('player.input')
    def test_select_position_if_human(self, mock_input):
        human = Player(is_human=True)
        human.select_position()
        mock_input.assert_called()

    def test_select_position_if_not_human(self):
        computer = Player(is_human=False)
        for i in range(10):
            self.assertTrue(1 <= computer.select_position() <= 9)
