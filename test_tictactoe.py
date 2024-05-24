from io import StringIO
from unittest import TestCase
from unittest.mock import patch
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