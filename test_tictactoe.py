from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from tictactoe import Tictactoe
from player import Player
from board import Board


@patch('sys.stdout', new_callable=StringIO)
class TestTictactoe(TestCase):

    def setUp(self):
        self.tictactoe = Tictactoe()

    def test_has_two_players(self, stdout):
        self.assertEqual(2, len(self.tictactoe.players))
        self.assertTrue(
            all(
                isinstance(player, Player) for player in self.tictactoe.players
            )
        )

    def test_player_1_is_human_and_player_2_is_not(self, stdout):
        self.assertTrue(self.tictactoe.players[0].is_human)
        self.assertFalse(self.tictactoe.players[1].is_human)

    def test_has_a_game_board(self, stdout):
        self.assertTrue(isinstance(self.tictactoe.board, Board))

    def test_display_board(self, stdout):
        self.tictactoe.board.positions = [
            1,'X', 3,
            'O', 5, 6,
            7, 8, 9,
        ]
        self.tictactoe.display_board()
        self.assertIn(
            ' 1 | X | 3 \n'
            '---+---+---\n'
            ' O | 5 | 6 \n'
            '---+---+---\n'
            ' 7 | 8 | 9 \n',
            stdout.getvalue()
        )

    def test_display_message(self, stdout):
        self.tictactoe.display_message('Hello')
        self.assertIn('Hello', stdout.getvalue())

    @patch.object(Player, 'select_position', side_effect=[1, None])
    def test_game_loop_ends_if_player_selection_is_None(
        self, mock_selection, stdout
    ):
        self.tictactoe.play()
        self.assertEqual(2, mock_selection.call_count)

    @patch.object(Player, 'select_position', side_effect=[1, 2, None])
    def test_game_loop_gets_selection_from_each_player(
        self, mock_selection, stdout
    ):
        self.tictactoe.play()
        self.assertTrue(
            all(p.select_position.called for p in self.tictactoe.players)
        )

    @patch.object(Tictactoe, 'display_board')
    @patch.object(Player, 'select_position', side_effect=[None])
    def test_board_displayed_at_the_start_of_the_game(
        self, mock_selection, mock_display_board, stdout
    ):
        self.tictactoe.play()
        self.assertEqual(1, mock_display_board.call_count)

    @patch.object(Tictactoe, 'display_board')
    @patch.object(Player, 'select_position', side_effect=[1, 2, None])
    def test_board_displayed_after_each_player_turn(
        self, mock_selection, mock_display_board, stdout
    ):
        self.tictactoe.play()
        self.assertEqual(3, mock_display_board.call_count)

    @patch.object(Player, 'select_position', side_effect=[None])
    def test_displays_user_selection_prompt_for_human_player(
        self, mock_selection, stdout
    ):
        self.tictactoe.play()
        self.assertIn('Enter your selection: ', stdout.getvalue())

    @patch.object(Player, 'select_position', side_effect=[1, None])
    def test_displays_user_selection_prompt_for_human_player(
        self, mock_selection, stdout
    ):
        self.tictactoe.play()
        self.assertIn("The computer selected `None'", stdout.getvalue())

    @patch.object(Player, 'select_position', side_effect=[None])
    def test_displays_welcome_message(self, mock_selection, stdout):
        self.tictactoe.play()
        self.assertIn('Starting tictactoe...', stdout.getvalue())

    @patch.object(Board, 'place_marker', side_effect=Exception())
    @patch.object(Player, 'select_position', side_effect=[1, None])
    def test_displays_message_if_place_marker_raises_exception(
        self, mock_selection, mock_place_marker, stdout
    ):
        self.tictactoe.play()
        self.assertIn(
            'Invalid selection, not placing marker.',
            stdout.getvalue()
        )

    @patch.object(Player, 'select_position', side_effect=[3, None])
    def test_displays_results_message_at_end_of_game_if_player_wins(
        self, mock_selection, stdout
    ):
        self.tictactoe.board.positions = [
            'X', 'X', 3,
            4, 5, 6,
            7, 8, 9,
        ]
        self.tictactoe.play()
        self.assertIn('You win!', stdout.getvalue())

    @patch.object(Player, 'select_position', side_effect=['Bleh', 3, None])
    def test_displays_results_message_at_end_of_game_if_player_loses(
        self, mock_selection, stdout
    ):
        self.tictactoe.board.positions = [
            'O', 'O', 3,
            4, 5, 6,
            7, 8, 9,
        ]
        self.tictactoe.play()
        self.assertIn('You lose!', stdout.getvalue())

    @patch.object(Board, 'is_full', return_value=True)
    @patch.object(Player, 'select_position', side_effect=[1, None])
    def test_displays_results_message_at_end_of_game_if_tiebreak(
        self, mock_selection, mock_is_full, stdout
    ):
        self.tictactoe.play()
        self.assertIn("It's a tie!", stdout.getvalue())
