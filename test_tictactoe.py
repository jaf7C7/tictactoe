from io import StringIO
from unittest import TestCase
from unittest.mock import patch, Mock
from tictactoe import Tictactoe


class TestTictactoe(TestCase):

    def setUp(self):
        self.tictactoe = Tictactoe(player_type=Mock, board_type=Mock)

    def test_has_a_player_X_and_a_player_O(self):
        self.assertTrue(
            hasattr(self.tictactoe, 'player_X')
            and hasattr(self.tictactoe, 'player_O')
        )

    def test_has_a_game_board(self):
        self.assertTrue(hasattr(self.tictactoe, 'board'))

    @patch('sys.stdout', new_callable=StringIO)
    def test_can_display_messages_to_user(self, stdout):
        self.tictactoe.display('Hello, World!')
        self.assertIn('Hello, World!', stdout.getvalue())

    def test_play_plays_rounds_until_the_game_is_over(self):
        self.tictactoe.play_round = Mock()
        self.tictactoe.game_over = Mock(side_effect=[False, False, True])
        self.tictactoe.play()
        self.assertEqual(2, self.tictactoe.play_round.call_count)

    def test_game_over_returns_true_if_the_board_is_full_or_a_winner_is_found(
        self
    ):
        for winning_marker, is_full, game_over in (
            ('X', True, True),
            ('X', False, True),
            (None, True, True),
            (None, False, False),
        ):
            self.tictactoe.board.configure_mock(
                winning_marker=Mock(return_value=winning_marker),
                is_full=Mock(return_value=is_full)
            )
            self.assertTrue(self.tictactoe.game_over() is game_over)