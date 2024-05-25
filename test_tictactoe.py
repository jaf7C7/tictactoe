from io import StringIO
from unittest import TestCase
from unittest.mock import patch, Mock
from tictactoe import Tictactoe


@patch('sys.stdout', new_callable=StringIO)
class TestTictactoe(TestCase):

    def setUp(self):
        self.tictactoe = Tictactoe(player_type=Mock, board_type=Mock)

    def test_has_two_players(self, stdout):
        self.assertTrue(
            hasattr(self.tictactoe, 'player_1')
            and hasattr(self.tictactoe, 'player_2')
        )

    def test_has_a_game_board(self, stdout):
        self.assertTrue(hasattr(self.tictactoe, 'board'))

    def test_can_display_messages_to_user(self, stdout):
        self.tictactoe.display('Hello, World!')
        self.assertIn('Hello, World!', stdout.getvalue())

    def test_play_loops_until_the_game_is_over(self, stdout):
        self.tictactoe.play_round = Mock()
        self.tictactoe.game_over = Mock(side_effect=[False, False, True])
        self.tictactoe.play()
        self.assertEqual(3, self.tictactoe.game_over.call_count)

    def test_game_over_returns_true_if_the_board_is_full_or_a_winner_is_found(
        self, stdout
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

    def test_play_calls_select_position_on_each_player(self, stdout):
        self.tictactoe.game_over = Mock(side_effect=[False, True])
        self.tictactoe.play()
        self.assertTrue(
            self.tictactoe.player_1.select_position.called
            and self.tictactoe.player_2.select_position.called
        )

    def test_play_calls_place_marker_for_each_player(self, stdout):
        self.tictactoe.game_over = Mock(side_effect=[False, True])
        self.tictactoe.play()
        self.assertEqual(2, self.tictactoe.board.place_marker.call_count)

    def test_play_displays_a_message_if_the_marker_cannot_be_placed(
        self, stdout
    ):
        self.tictactoe.game_over = Mock(side_effect=[False, True])
        self.tictactoe.board.place_marker.configure_mock(
            side_effect=Exception()
        )
        self.tictactoe.play()
        self.assertIn(
            'Position not available, cannot place marker.',
            stdout.getvalue()
        )

    def test_play_displays_the_winner_if_winner_is_not_none(
        self, stdout
    ):
        self.tictactoe.game_over = Mock(side_effect=[True])
        self.tictactoe.winner = 'X'
        self.tictactoe.play()
        self.assertIn('The winner is... `X`!', stdout.getvalue())
