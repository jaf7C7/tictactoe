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

    @patch.object(
        Player,
        'select_position',
        side_effect=[1, 4, 2, 5, 3, None]
    )
    def test_play(self, mock_selection, stdout):
        self.tictactoe.play()
        self.assertIn(
            'Starting tictactoe...\n'
            ' 1 | 2 | 3 \n'
            '---+---+---\n'
            ' 4 | 5 | 6 \n'
            '---+---+---\n'
            ' 7 | 8 | 9 \n'
            'Enter your selection: '
            ' X | 2 | 3 \n'
            '---+---+---\n'
            ' 4 | 5 | 6 \n'
            '---+---+---\n'
            ' 7 | 8 | 9 \n'
            "The computer selected `4'\n"
            ' X | 2 | 3 \n'
            '---+---+---\n'
            ' O | 5 | 6 \n'
            '---+---+---\n'
            ' 7 | 8 | 9 \n'
            'Enter your selection: '
            ' X | X | 3 \n'
            '---+---+---\n'
            ' O | 5 | 6 \n'
            '---+---+---\n'
            ' 7 | 8 | 9 \n'
            "The computer selected `5'\n"
            ' X | X | 3 \n'
            '---+---+---\n'
            ' O | O | 6 \n'
            '---+---+---\n'
            ' 7 | 8 | 9 \n'
            'Enter your selection: '
            ' X | X | X \n'
            '---+---+---\n'
            ' O | O | 6 \n'
            '---+---+---\n'
            ' 7 | 8 | 9 \n'
            'You win!\n',
            stdout.getvalue()
        )
