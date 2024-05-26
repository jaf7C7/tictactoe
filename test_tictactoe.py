from io import StringIO
from unittest import TestCase
from unittest.mock import patch, Mock
from tictactoe import Tictactoe


@patch('sys.stdout', new_callable=StringIO)
class TestTictactoe(TestCase):

    def setUp(self):
        self.tictactoe = Tictactoe(player_type=Mock, board_type=Mock)

    def test_has_an_X_and_an_O_player(self, stdout):
        self.assertTrue(
            self.tictactoe.player_X.marker == 'X'
            and self.tictactoe.player_O.marker == 'O'
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
            self.tictactoe.player_X.select_position.called
            and self.tictactoe.player_O.select_position.called
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

    def test_play_displays_the_result_when_the_game_is_over(
        self, stdout
    ):
        self.tictactoe.game_over = Mock(return_value=True)
        for winner, msg in (
            ('X', '\n**** `X` wins! ****\n'),
            (None, "\n**** It's a tie! ****\n")
        ):
            self.tictactoe.winner = winner
            self.tictactoe.play()
            self.assertIn(msg, stdout.getvalue())

    def test_play_displays_a_prompt_for_user_input_if_the_player_is_human(
        self, stdout
    ):
        self.tictactoe.game_over = Mock(side_effect=[False, True])
        self.tictactoe.player_X.is_human = True
        self.tictactoe.play()
        self.assertIn('Select an available position: ', stdout.getvalue())

    def test_play_displays_the_board_once_per_player_turn(self, stdout):
        self.tictactoe.game_over = Mock(side_effect=[False, True])
        self.tictactoe.play()
        self.assertEqual(2, stdout.getvalue().count(str(self.tictactoe.board)))

    def test_play_displays_a_message_for_each_computer_selection(self, stdout):
        self.tictactoe.game_over = Mock(side_effect=[False, True])
        self.tictactoe.play()
        self.assertIn('The computer selected position ', stdout.getvalue())

    def test_play_displays_a_welcome_message(self, stdout):
        self.tictactoe.game_over = Mock(side_effect=[True])
        self.tictactoe.play()
        self.assertIn(
            'Welcome to Tic-Tac-Toe!\n'
            '=======================\n',
            stdout.getvalue()
        )
