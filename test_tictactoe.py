from unittest import TestCase
from tictactoe import Tictactoe


class TestTictactoe(TestCase):

    def setUp(self):
        self.tictactoe = Tictactoe()

    def test_has_a_human_player(self):
        self.assertTrue(
            hasattr(self.tictactoe, 'player')
            and self.tictactoe.player.is_human
        )

    def test_has_a_computer_player(self):
        self.assertTrue(
            hasattr(self.tictactoe, 'computer')
            and not self.tictactoe.computer.is_human
        )
