from unittest import TestCase
from tictactoe import Tictactoe


class TestTictactoe(TestCase):

    def setUp(self):
        self.tictactoe = Tictactoe()

    def test_has_two_players(self):
        self.assertEqual(2, len(self.tictactoe.players))
