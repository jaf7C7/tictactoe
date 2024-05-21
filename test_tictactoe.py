from unittest import TestCase
from unittest.mock import patch
from tictactoe import Tictactoe
from player import Player
from board import Board


class TestTictactoe(TestCase):

    def setUp(self):
        self.tictactoe = Tictactoe()

    def test_has_two_players(self):
        self.assertEqual(2, len(self.tictactoe.players))
        self.assertTrue(
            all(
                isinstance(player, Player) for player in self.tictactoe.players
            )
        )

    def test_player_1_is_human_and_player_2_is_not(self):
        self.assertTrue(self.tictactoe.players[0].is_human)
        self.assertFalse(self.tictactoe.players[1].is_human)

    def test_has_a_game_board(self):
        self.assertTrue(isinstance(self.tictactoe.board, Board))

    @patch.object(Player, 'select_position', side_effect=['Blah', None])
    def test_game_loop_ends_if_player_selection_is_None(self, mock_selection):
        self.tictactoe.play()
        self.assertEqual(2, mock_selection.call_count)
