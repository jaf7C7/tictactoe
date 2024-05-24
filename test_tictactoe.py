from io import StringIO
from unittest import TestCase
from unittest.mock import patch, Mock
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

    def test_has_a_game_board(self):
        self.assertTrue(hasattr(self.tictactoe, 'board'))

    @patch('sys.stdout', new_callable=StringIO)
    def test_can_display_messages_to_user(self, stdout):
        self.tictactoe.display('Hello, World!')
        self.assertIn('Hello, World!', stdout.getvalue())

    def test_play_plays_rounds_until_a_winning_marker_is_found(self):
        self.tictactoe.play_round = Mock()
        self.tictactoe.game_over = Mock(side_effect=[False, True])
        self.tictactoe.play()
        self.assertEqual(1, self.tictactoe.play_round.call_count)
