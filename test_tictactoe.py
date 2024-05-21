from unittest import TestCase
from tictactoe import Tictactoe


class TestTictactoe(TestCase):

    def setUp(self):
        self.tictactoe = Tictactoe()

    def test_has_two_players(self):
        self.assertEqual(2, len(self.tictactoe.players))

    def test_players_implement_select_position(self):
        self.assertTrue(
            all(
                hasattr(player, 'select_position')
                for player in self.tictactoe.players
            )
        )
